from os import getenv

class Config:
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    MONGO_URI = getenv('MONGO_URI')
    MONGO_DATABASE = getenv('MONGO_DATABASE')

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': DevelopmentConfig
}
