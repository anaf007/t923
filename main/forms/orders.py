#coding=utf-8
from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField,IntegerField,BooleanField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    """提交订单表单."""
    name = StringField(u'收货人姓名', validators=[DataRequired()])
    phone = StringField(u'收货人电话', validators=[DataRequired()])
    address = StringField(u'收货人地址', validators=[DataRequired()])



