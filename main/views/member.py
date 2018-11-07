#coding=utf-8
from flask import request,url_for,flash,redirect,Blueprint
from main.decorators import admin_required
from main.helpers import templated
from main.utils import flash_errors
from main.models.users import User
from flask_login import login_required,current_user
from main.forms.auth import RegisterForm
from main.models.products import Product
from main.models.users import User
from main.models.recommend import Recommend
from main.routes.menber import reg_url

bp = Blueprint('member', __name__,url_prefix='/member')
reg_url(bp)

@admin_required
@templated()
def home():
    return dict()


@admin_required
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

