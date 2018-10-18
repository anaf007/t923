# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user,current_user

from main.public.forms import LoginForm
from .forms import RegisterForm
from main.models.users import User
from main.models.recommend import Recommend
from main.models.products import Product
from main.utils import flash_errors
from main.helpers import templated
from log import logger

import simplejson as json


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




@templated()
def about():
    """About page."""
    form = LoginForm(request.form)
    return dict(form=form)
