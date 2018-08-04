#coding=utf-8
from flask_wtf import Form
from wtforms.ext.appengine.db import model_form
from wtforms import validators
from .models import SysConfig

"""http://flask.pocoo.org/snippets/60/
Automatically create a WTForms Form from model
"""
SysConfigForm = model_form(SysConfig, Form, field_args = {
    'web_name' : {
        'validators' : [validators.Length(max=5)]
    }
})


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