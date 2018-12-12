# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, render_template

from main import commands, views
from main.extensions import bcrypt, cache, csrf_protect, db, \
    debug_toolbar, login_manager, migrate, bootstrap, apiManager, rbac
# from main.settings import ProdConfig
# from main import models

from main.models.users import User



from .blueprints import register_blueprints


def create_app(config_object='main.settings'):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0],static_folder='../static',template_folder='../tpl')
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    

    # from main import api


    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.app = app
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    # redis_store.init_app(app)
    # db.app = app
    register_api_blueprints(app)
    apiManager.init_app(app)
    rbac.init_app(app)
    # principal.init_app(app)
    bootstrap.init_app(app)
    return None




def register_api_blueprints(app):
    """Register apiManager blueprints. """   
    apiManager.create_api(User,methods=['GET', 'POST', 'DELETE'],primary_key='id')
    # app.register_blueprint(blueprint) 


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {'db': db}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
    app.cli.add_command(commands.init_databases)



