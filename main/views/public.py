# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user,current_user
from main.helpers import templated
from main.forms.auth import LoginForm,RegisterForm
from main.models.users import User
from main.models.recommend import Recommend
from main.models.products import Product
from main.models.buys_car import BuysCar
from main.utils import flash_errors
from main.tools.log import logger
from main.routes.public import reg_url
import simplejson as json


bp = Blueprint('public', __name__)
reg_url(bp)


@templated()
def home():
    """Home page."""
    products = Product().get_all()
    return dict(products=products)


@login_required
@templated()
def add_buy_car(id):
    """添加购物车."""
    result = BuysCar.query.filter_by(users=current_user,product_id=id).first()
    if result:
        result.update(count=result.count+1)
    else:
        BuysCar.create(
            add_price = 0.00,
            product_id = id,
            count = 1,
            users = current_user,
        )
        flash("添加成功")
    return dict()

    
def home_json():
    return json.dumps({'data':[[1,2],[2,3],[3,4]]})

@templated()
def about():
    """About page."""
    form = LoginForm(request.form)
    return dict(form=form)






