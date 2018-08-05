# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from main.public.forms import LoginForm
from main.user.forms import RegisterForm
from main.user.models import User
from main.utils import flash_errors
from main.helpers import templated
from log import logger


@login_required
@templated()
def home():
    """Home page."""
    return dict()


@templated()
def login():
    """login."""
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            logger.info('===ID:'+str(current_user.id)+'-login')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)

    return dict(form=form)


@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@templated()
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(username=form.username.data,password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return dict(form=form)


@templated()
def about():
    """About page."""
    form = LoginForm(request.form)
    return dict(form=form)
