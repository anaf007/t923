# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_sse import sse
from flask_redis import FlaskRedis
from concurrent.futures import ThreadPoolExecutor
# from flask_rbac import RBAC
from flask_principal import Principal
from flask_bootstrap import Bootstrap
# from flask_restful import Api
from flask_restless import APIManager

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
redis_store = FlaskRedis()
executor = ThreadPoolExecutor(2)
# rbac = RBAC()
principal = Principal()
bootstrap = Bootstrap()
# api = Api(decorators=[csrf_protect.exempt])
apiManager = APIManager(flask_sqlalchemy_db=db,decorators=[csrf_protect.exempt])

login_manager.session_protection = 'basic'

#自动注册
login_manager.login_view = 'public.login'
login_manager.login_message = "请登录后访问该页面."
login_manager.refresh_view = 'public.login'
