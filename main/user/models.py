# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
from main.extensions import bcrypt
# from flask_rbac import RoleMixin


class Permission:
    ADMINISTER = 0x8000  #管理员权限


# @rbac.as_role_model
class Role(SurrogatePK,Model):
    """A role for a user."""

    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # user_id = reference_col('users', nullable=True)
    # user = relationship('User', backref='roles')
    # parents = db.relationship(
    #     'Role',
    #     secondary='roles_parents',
    #     primaryjoin=('id == roles_parents.c.role_id'),
    #     secondaryjoin=('id == roles_parents.c.parent_id'),
    #     backref=db.backref('children', lazy='dynamic'),
    # )

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    # def __init__(self, name):
    #     RoleMixin.__init__(self)
    #     self.name = name


    # def __repr__(self):
    #     """Represent instance as a unique string."""
    #     return '<Role({name})>'.format(name=self.name)

    # def add_parent(self, parent):
    #     # You don't need to add this role to parent's children set,
    #     # relationship between roles would do this work automatically
    #     self.parents.append(parent)

    # def add_parents(self, *parents):
    #     for parent in parents:
    #         self.add_parent(parent)

    # @staticmethod
    # def get_by_name(name):
    #     return Role.filter_by(name=name).first()


# anonymous = Role('anonymous')
# rbac.set_role_model(Role)


# @rbac.as_user_model
class User(UserMixin, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.Binary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    # roles = db.relationship(
    #     'Role',
    #     secondary='users_roles',
    #     backref=db.backref('roles', lazy='dynamic')
    # )

    # def __init__(self, username, email, password=None, **kwargs):
    #     """Create instance."""
    #     db.Model.__init__(self, username=username, email=email, **kwargs)
    #     if password:
    #         self.set_password(password)
    #     else:
    #         self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)

    def add_role(self, role):
        self.roles.append(role)

    def add_roles(self, roles):
        for role in roles:
            self.add_role(role)

    def get_roles(self):
        for role in self.roles:
            yield role


# a_user = User()
# rbac.set_user_model(User)


# roles_parents = db.Table(
#     'roles_parents',
#     db.Column('role_id', db.Integer, db.ForeignKey('roles.id'),nullable=True),
#     db.Column('parent_id', db.Integer, db.ForeignKey('roles.id'),nullable=True)
# )

# users_roles = db.Table(
#     'users_roles',
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#     db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
# )



