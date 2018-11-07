# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
from main.extensions import bcrypt
# from flask_rbac import RoleMixin


class Permission:
    ADMINISTER = 0x8000  #管理员权限














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



