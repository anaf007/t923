#coding=utf-8

from flask import Blueprint,session,current_app
from main.helpers import LazyView
from main.extensions import executor
from .fck import publish_cpu,onlinr_users
import psutil

bp = Blueprint('admin', __name__,url_prefix='/admin')

from . import routes,views



#在每个请求之前执行这样的功能，即使在蓝图之外也是如此。
# @bp.before_app_request
# def before_app_request():
#     print('before_app_request')

# @bp.context_processor
# def get_psutil():  
#     return dict(psutil=psutil)

#每个请求之前执行。
@bp.before_request
def before_request():
    #回话超时登出
    session.permanent = True

    #cpu状态
    executor.submit(publish_cpu,current_app._get_current_object(),True)
    #在线人数
    executor.submit(onlinr_users,current_app._get_current_object(),True)


    # print('before_request')



