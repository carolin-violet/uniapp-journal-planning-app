"""
配置文件
"""

SQLALCHEMY_POOL_RECYCLE = 1
SQLALCHEMY_POOL_SIZE = 30
SQLALCHEMY_TRACK_MODIFICATIONS = True
DIALCT = "mysql"
DRIVER = "pymysql"
USERNAME = "root"
PASSWORD = "zj20001125"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "forEfficient"


class Config(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
