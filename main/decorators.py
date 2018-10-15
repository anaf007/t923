#coding=utf-8
from functools import wraps
from flask import abort, flash, redirect, url_for, request
from flask_login import current_user
from main.user.models  import Permission


def permission_required(permission):
    
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                flash('您没有权限访问。')
                abort(401)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        # if request.url_root != current_app.config['SUPERADMIN_WEB_URL']:
        #     abort(404)
        if not current_user.is_authenticated:
            return redirect(url_for('public.login',next='/admin'))
        else:
            if not current_user.is_administrator():
                abort(404)
        return func(*args, **kwargs)

    return decorator
