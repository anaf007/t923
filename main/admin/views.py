#coding=utf-8
from main.helpers import templated,get_online_users
from flask_login import login_required,current_user
from flask import Response,current_app,request,flash
from flask_sse import sse
import psutil
from time import sleep
from . import bp


from main.decorators import admin_required

from .forms import ProductsForm
from ..models.products import Product
from main.models.users import User


@admin_required
@templated()
def home():

    
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


@admin_required
@templated()
def index(name='admin'):
    return dict()


@admin_required
@templated()
def web_site():
    """站点管理，站点信息"""
    return dict()



@admin_required
@templated()
def add_products():
    """添加产品"""
    form = ProductsForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            Product.create(
                name = form.name.data,
                price = form.price.data,
            )
            flash('添加成功。','success')
        else:
            flash('数据校验失败','danger')

    return dict(form=form)



