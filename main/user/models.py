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

    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)


class Recommend(Model):
    """用户推荐表."""
    __tablename__ = 'recommend'
    #推荐人
        # recommend_id = reference_col('users.id')
        # #被推荐人
        # recommender_id = reference_col('users.id')
    timestamp = db.Column(db.DateTime, default=dt.datetime.now)
    #被推荐人
    recommender_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        primary_key=True)
    #推荐人
    recommends_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        primary_key=True)



class User(UserMixin, SurrogatePK, Model):
    """用户表."""
    __tablename__ = 'users'

    username = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.Binary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    first_name = Column(db.String(30))
    last_name = Column(db.String(30))
    active = Column(db.Boolean(), default=False)
    #激活时间
    active_at = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    is_admin = Column(db.Boolean(), default=False)
    #是否报单中心
    is_center = Column(db.Boolean(), default=False)
    #手机号码唯一 可用于登录
    phone = Column(db.String(30),unique=True)

    buys_id = relationship('ProductsBuys', backref='user')

    #:引用自身,保单中心
    parent_center = reference_col('users')
    children_center = relationship("User",join_depth=2,lazy="joined",post_update=True)

    #推荐人
    recommends = db.relationship('Recommend',
        foreign_keys=[Recommend.recommender_id],
        backref=db.backref('recommender', lazy='joined'),
        lazy='dynamic',cascade='all, delete-orphan')
    recommender = db.relationship('Recommend',
        foreign_keys=[Recommend.recommends_id],
        backref=db.backref('recommends', lazy='joined'),
        lazy='dynamic',cascade='all, delete-orphan')

    def __init__(self, username, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username,**kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

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

    #管理员
    def is_administrator(self):
        return self.is_admin 

    # def add_role(self, role):
    #     self.roles.append(role)

    # def add_roles(self, roles):
    #     for role in roles:
    #         self.add_role(role)

    # def get_roles(self):
    #     for role in self.roles:
    #         yield role

    def init_insert():
        User.create(username='admin', password='a0000000', active=True)
        






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



