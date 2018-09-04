#coding=utf-8
from flask_wtf import Form
from flask_wtf import FlaskForm
# from wtforms.ext.appengine.db import model_form
from wtforms import validators
from .models import SysConfig,Products
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms import PasswordField, StringField,SelectField
from wtforms.validators import DataRequired

"""http://flask.pocoo.org/snippets/60/
Automatically create a WTForms Form from model
"""
SysConfigForm = model_form(SysConfig, base_class=Form)


class ProductsForm(FlaskForm):
    """Login form."""

    name = StringField('产品名称：', validators=[DataRequired()],render_kw={'class':"layui-input"})
    price = StringField('产品价格：', validators=[DataRequired()],render_kw={'class':'layui-input'})

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(ProductsForm, self).__init__(*args, **kwargs)
    
        

    def validate(self):
        """Validate the form."""
        initial_validation = super(ProductsForm, self).validate()
        if not initial_validation:
            return False
        
        return True

    

"""example:

from flaskext.wtf import Form
from wtforms.ext.appengine.db import model_form
from models import MyModel

@app.route("/edit<id>")
def edit(id):
    MyForm = model_form(MyModel, Form)
    model = MyModel.get(id)
    form = MyForm(request.form, model)

    if form.validate_on_submit():
        form.populate_obj(model)
        model.put() 
        flash("MyModel updated")
        return redirect(url_for("index"))
    return render_template("edit.html", form=form)
    
"""