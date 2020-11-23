import os

basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    """Base configuration"""
    MONGO_INITDB_USERNAME = os.environ["MONGO_INITDB_USERNAME"]
    MONGO_INITDB_PASSWORD = os.environ["MONGO_INITDB_PASSWORD"]
    MONGO_INITDB_DATABASE = os.environ["MONGO_INITDB_DATABASE"]
    MONGO_INITDB_HOSTNAME = os.environ["MONGO_INITDB_HOSTNAME"]
    MONGO_INITDB_PORT = os.environ["MONGO_INITDB_PORT"]
    


class ProductionConfig(Config):
    """Production configuration"""

class DevelopmentConfig(Config):
    """Development configuration"""
    

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True