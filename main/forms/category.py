#coding=utf-8
from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField,IntegerField,BooleanField
from wtforms.validators import DataRequired

class CategoryForm(FlaskForm):
    """产品分类表单."""

    name = StringField('分类名称：', validators=[DataRequired()],render_kw={'class':"layui-input"})
    sort = IntegerField('分类排序：', validators=[DataRequired()],render_kw={'class':'layui-input'})

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(CategoryForm, self).__init__(*args, **kwargs)
    
    def validate(self):
        """Validate the form."""
        initial_validation = super(CategoryForm, self).validate()

        if not initial_validation:
            return False
        
        return True
