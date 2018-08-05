# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from datetime import timedelta

class Config(object):
    """Base configuration."""

    # import os
    # os.urandom(24)
    SECRET_KEY = os.environ.get('MAIN_SECRET', 'secret-key')  

    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #api返回中文
    JSON_AS_ASCII = False

    #回话超时登出 分钟
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)

    #redis配置
    REDIS_URL = 'redis://:@localhost:6379'
    ONLINE_LAST_MINUTES = 10

    #验证码
    VERIFICATION_CODE_FONT = os.environ.get('CN_CMS_VERIFICATION_CODE_FONT') or 'Arial.ttf'


    RBAC_USE_WHITE = True



class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/t923'
    DEBUG_TB_ENABLED = True
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
