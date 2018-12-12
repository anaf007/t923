#coding=utf-8
from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
from main.extensions import bcrypt,rbac
from flask_rbac import RoleMixin

class Permission:
    ADMINISTER = 0x8000  #管理员权限


roles_parents = db.Table(
    'roles_parents',
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
    db.Column('parent_id', db.Integer, db.ForeignKey('roles.id'))
)


@rbac.as_role_model
class Role(SurrogatePK,Model,RoleMixin):
    """A role for a user."""

    __tablename__ = 'roles'

    name = db.Column(db.String(80))
    parents = db.relationship(
        'Role',
        secondary=roles_parents,
        primaryjoin=("Role.id == roles_parents.c.role_id"),
        secondaryjoin=("Role.id == roles_parents.c.parent_id"),
        backref=db.backref('children', lazy='dynamic')
    )


    def __init__(self, name):
        RoleMixin.__init__(self)
        self.name = name

    def add_parent(self, parent):
        # You don't need to add this role to parent's children set,
        # relationship between roles would do this work automatically
        self.parents.append(parent)

    def add_parents(self, *parents):
        for parent in parents:
            self.add_parent(parent)

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()


anonymous = Role('anonymous')



