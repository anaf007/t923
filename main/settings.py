# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env
from datetime import timedelta

env = Env()
env.read_env()

ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SQLALCHEMY_DATABASE_URI = env.str('DATABASE_URL')
# import os
# os.urandom(24)
SECRET_KEY = env.str('SECRET_KEY')
BCRYPT_LOG_ROUNDS = env.int('BCRYPT_LOG_ROUNDS', default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'

WTF_CSRF_CHECK_DEFAULT = False



#api返回中文
JSON_AS_ASCII = False

#回话超时登出 分钟
PERMANENT_SESSION_LIFETIME = timedelta(minutes=100)

#redis配置
REDIS_URL = 'redis://:@localhost:6379'
#在线时间
ONLINE_LAST_MINUTES = 10

#验证码
# VERIFICATION_CODE_FONT = os.environ.get('VERIFICATION_CODE_FONT') or 'Arial.ttf'
VERIFICATION_CODE_FONT = 'C:\\Windows\\Fonts\\arial.ttf'

RBAC_USE_WHITE = True


