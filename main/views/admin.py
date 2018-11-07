#coding=utf-8
from main.helpers import templated,get_online_users
from flask_login import login_required,current_user
from flask import Response,current_app,request,flash,Blueprint
from flask_sse import sse
import psutil
from time import sleep

from main.decorators import admin_required
from main.routes.admin import reg_url
from main.forms.products import ProductsForm
from ..models.products import Product,Category
from main.models.users import User
from main.forms.category import CategoryForm

bp = Blueprint('admin', __name__,url_prefix='/admin')
#注册路由
reg_url(bp)

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
                category_id = form.category.data
            )
            flash('添加成功。','success')
            form.name.data = ''
            form.price.data = ''
        else:
            flash('数据校验失败','danger')

    return dict(form=form)


@admin_required
@templated()
def all_products():
    return dict()



@admin_required
@templated()
def add_category():
    """添加产品分类"""
    form = CategoryForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            Category.create(
                name = form.name.data,
                sort = form.sort.data,
            )
            flash('添加成功。','success')
            form.name.data = ''
            form.sort.data = '10'
        else:
            flash('数据校验失败','danger')

    return dict(form=form)