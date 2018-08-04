#coding=utf-8
from main.helpers import templated,get_online_users
from flask_login import login_required
from flask import Response,current_app,copy_current_request_context
from flask_sse import sse
import psutil
from time import sleep
from . import bp,admin_permission
from main.extensions import executor
from .fck import publish_cpu,onlinr_users
from main.decorators import admin_required

@templated()
def home():

    executor.submit(publish_cpu,current_app._get_current_object(),True)
    executor.submit(onlinr_users,current_app._get_current_object(),True)

    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')


    use_mem = mem.total-mem.available

    return dict(
        online_count=0,
        psutil=psutil,
        mem=mem,
        disk=disk,
        use_mem=use_mem//1024//1024
    )


# @login_required
@templated()
def index(name='admin'):
    return dict()


@login_required
@templated()
def web_site():
    return dict()



