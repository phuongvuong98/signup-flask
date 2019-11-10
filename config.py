import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root@localhost:3306/signup?charset=utf8mb4"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = "enable"
    MYSQL_DATABASE_CHARSET = 'utf8mb4'
    SESSION_TYPE = 'memcached'
    SECRET_KEY = 'top secret'
    OAUTH_CREDENTIALS = {
        'facebook': {
            'id': '441928096353531',
            'secret': 'c34e5e154b6f06cbd9ff5faf397d0981',
            'callbackUrl': 'https://dcb8d6c5.ngrok.io/callback/facebook'
        },
        'twitter': {
            'id': 'ISds3P54QFGMFlnIUvvsz1Oxo',
            'secret': 'j49QBzc7YqNHuZFNO2YuFcqGcWL1Vn4bEI3UQoOaZEDuRmZN5S',
            'callbackUrl': 'https://dcb8d6c5.ngrok.io/callback/twitter'
        }
    }


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
