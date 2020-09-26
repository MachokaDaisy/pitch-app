import os

class Config:
    '''
    contains general configuration code
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daisy:4H@ppyfeet@localhost/pitch'

class ProdConfig(Config):
    '''
    subclass of Config with configurations for production mode
    '''
    pass

class DevConfig(Config):
    '''
    subclass of config class with configurations for development mode
    '''
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}