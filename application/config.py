import os

basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    """Base configuration"""
    user = os.environ["MONGO_INITDB_ROOT_USERNAME"]
    password = os.environ["MONGO_INITDB_ROOT_PASSWORD"]
    database = os.environ["MONGO_INITDB_DATABASE"]


class ProductionConfig(Config):
    """Production configuration"""

class DevelopmentConfig(Config):
    """Development configuration"""

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True