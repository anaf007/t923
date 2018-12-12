# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint,request
from flask_login import login_required,current_user
from main.routes.users import reg_url
from main.helpers import templated
from main.utils import flash_errors
from main.models.buys_car import BuysCar
from main.models.products import Product
from main.forms.orders import SubmitForm
from main.plugins import executor
from main.extensions import rbac
# from main.function.order import back_submit_order
bp = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
reg_url(bp)


@rbac.deny(['logged_user'], methods=['GET', 'POST'])
@templated()
def home():
    """用户主页"""
    return dict()


@templated()
@login_required
def buys_car():
    """购物车"""
    car = BuysCar.query\
            .with_entities(BuysCar.id,BuysCar.count,Product.name,Product.price)\
            .join(Product,Product.id==BuysCar.product_id)\
            .filter(BuysCar.users==current_user)\
            .all()
    return dict(car=car)


@templated()
@login_required
def submit_order():
    """提交订单"""
    car = BuysCar.query\
            .with_entities(BuysCar.id,BuysCar.count,Product.name,Product.price)\
            .join(Product,Product.id==BuysCar.product_id)\
            .filter(BuysCar.users==current_user)\
            .all()
    form = SubmitForm()
    if not request.method == 'POST':
        return dict(car=car,form=form)

    # if form.validate_on_submit():
    #     executor.submit(back_submit_order,current_app._get_current_object(),args_list,db)



    
