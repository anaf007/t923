# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user,current_user

from main.public.forms import LoginForm
from .forms import RegisterForm
from main.user.models import User,Recommend
from main.admin.models import ProductsBuys,Products
from main.utils import flash_errors
from main.helpers import templated
from log import logger

import simplejson as json


@login_required
@templated()
def home():
    """Home page."""
    return dict()



def home_json():
    return json.dumps({'data':[[1,2],[2,3],[3,4]]})



@templated()
def login():
    """login."""
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('登录成功.', 'success')
            logger.info('===ID:'+str(current_user.id)+'-login')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            form.verification_code.data = ''
            flash_errors(form)

    return dict(form=form)


@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@login_required
@templated()
def add_users():
    """Register new user.
    获取产品
    添加用户
    添加到推荐人列表
    添加购买列表
    """
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        if current_user.is_admin or current_user.is_center:

            tuijianren = User.query.filter_by(phone=form.tuijianren.data).first()
            if not tuijianren:
                flash('已注册失败.推荐人不存在，请填写正确的手机号。', 'danger')
                return dict(form=form)
            baodan = User.query.filter_by(phone=form.baodan.data).first()
            if not tuijianren:
                flash('已注册失败.报单中心不存在，请填写正确的手机号。', 'danger')
                return dict(form=form)

            print(baodan)

            product = Products.query.get_or_404(int(form.products.data))
            user =User.create(
                username=form.user.data,
                password=form.password.data,
                phone=form.user.data, 
                active=False,
                parent_center=baodan.id
            )
            ProductsBuys.create(
                user=user,
                product=product,
            )
            Recommend.create(
                recommender_id=tuijianren.id,
                recommends_id=user.id
            )
            flash('已注册成功.', 'success')
        else:
            flash('已注册失败.您不是报单中心。', 'danger')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return dict(form=form)


@templated()
def about():
    """About page."""
    form = LoginForm(request.form)
    return dict(form=form)
