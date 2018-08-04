#coding=utf-8

from flask import Blueprint,session
from main.helpers import LazyView
from flask_principal import Permission, RoleNeed
# Create a permission with a single Need, in this case a RoleNeed.
admin_permission = Permission(RoleNeed('admin'))


bp = Blueprint('admin', __name__,url_prefix='/admin')

from . import routes,views,models


#在每个请求之前执行这样的功能，即使在蓝图之外也是如此。
# @bp.before_app_request
# def before_app_request():
#     print('before_app_request')


#每个请求之前执行。
@bp.before_request
def before_request():
    #回话超时登出
    session.permanent = True

    # print('before_request')



