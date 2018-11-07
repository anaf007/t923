
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,SelectField

from wtforms.validators import DataRequired, Email, EqualTo, Length,Required

from main.models.users import User

from flask import session
from sqlalchemy import or_
from main.models.products import Product


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    verification_code = StringField(u'验证码', validators=[DataRequired(), Length(4, 4, message=u'填写4位验证码')],render_kw={'style':'width:100px;'})


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
        print(self.username.data)
        self.user = User.query.filter(or_(User.username==self.username.data,User.phone==self.username.data)).first()
        print(self.user)
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



class RegisterForm(FlaskForm):
    """Register form."""

    user = StringField('手机号码',
                           validators=[DataRequired(), Length(min=3, max=25)],render_kw={'class':"layui-input",'placeholder':"请输入您的手机号码"})
    password = PasswordField('密码',
                             validators=[DataRequired(), Length(min=6, max=40)],render_kw={'class':"layui-input",'placeholder':"请输入您的密码"})
    confirm = PasswordField('确认密码',
                            [DataRequired(), EqualTo('password', message='密码不匹配')],render_kw={'class':"layui-input",'placeholder':"请再次输入您的密码"})
    password_two = PasswordField('密码',
                             validators=[DataRequired(), Length(min=6, max=40)],render_kw={'class':"layui-input",'placeholder':"请输入您的密码"})
    
    tuijianren = StringField('推荐人',
                           validators=[DataRequired(), Length(min=3, max=25)],render_kw={'class':"layui-input",'placeholder':"请输入推荐人的手机号码"})
    baodan = StringField('报单中心',
                           validators=[DataRequired(), Length(min=3, max=25)],render_kw={'class':"layui-input",'placeholder':"请输入报单中心的手机号码"})
    # products = SelectField(u'产品列表',coerce=int,validators=[DataRequired(message=u'请选择正确的产品')],render_kw={'class':"layui-input"})


    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        # self.products.choices = [(obj.id,[obj.price,obj.name]) for obj in Product.query.order_by('id').all()]
    
        

    def validate(self):
        """Validate the form."""
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(phone=self.user.data).first()
        if user:
            self.user.errors.append('该手机号码已经存在')
            return False
        return True

