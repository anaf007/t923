# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

from wtforms.validators import DataRequired, Email, EqualTo, Length,Required

from main.user.models import User

from flask import session


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    verification_code = StringField('验证码', validators=[DataRequired(), Length(4, 4, message=u'填写4位验证码')],render_kw={'style':'width:100px;'})


    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        try:
            if self.verification_code.data.upper() != session['verify']:
                self.verification_code.errors.append(u'输入不错误')
                return False
        except Exception as e:
            self.verification_code.errors.append(u'输入不错误')
            return False

        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append('没有该用户')
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append('密码不正确')
            return False

        if not self.user.active:
            self.username.errors.append('该用户没有激活')
            return False
        return True


"""
class RegisterForm(FlaskForm):
    username = StringField('用户名', validators={DataRequired(), render_kw={'placeholder':'your account','style':'text-align: center'})
    password = PasswordField('密码',validators=[DataRequired(),render_kw={'placeholder':'your password','style':'text-align: center'})
    confirm = PasswordField('确认密码',validators=[EqualTo('password',message='两次密码不一至')],render_kw={'placeholder':'your password agin','style':'text-align: center'})
    email = StringField('邮箱',validators=[Email(message='邮箱格式不正确')],render_kw={'placeholder':'example@163.com','style':'text-align: center'})
    submit = SubmitField('立即注册')
#注意这里的render_kw的使用方法
#它其实就是给我们的css添加我们需要的样式，是不是很神奇。
"""