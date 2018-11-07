#coding=utf-8
from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired
from main.models.products import Category


class ProductsForm(FlaskForm):
    """产品表单。"""

    name = StringField('产品名称：', validators=[DataRequired()],render_kw={'class':"layui-input"})
    price = StringField('产品价格：', validators=[DataRequired()],render_kw={'class':'layui-input'})
    category = SelectField('产品分类',coerce=int,)

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(ProductsForm, self).__init__(*args, **kwargs)

        self.category.choices = [(g.id, g.name) for g in Category.query.order_by('id').all()]
    
        

    def validate(self):
        """Validate the form."""
        initial_validation = super(ProductsForm, self).validate()
        if not initial_validation:
            return False
        
        return True

    