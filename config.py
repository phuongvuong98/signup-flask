import os


# default config
class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root@localhost:3306/signup?charset=utf8mb4"
    # SQLALCHEMY_DATABASE_URI = "postgres://vvongaztvgdcig:3fd18b29bea7ca1ec77dc1bf56841caf384fbee43705a63133fe924d0188cb36@ec2-23-21-87-183.compute-1.amazonaws.com:5432/signup?charset=utf8mb4"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = "enable"
    MYSQL_DATABASE_CHARSET = 'utf8mb4'

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
