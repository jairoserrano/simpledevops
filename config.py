import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'OrmucoTestDev'
    SQLALCHEMY_DATABASE_URI = "sqlite:///../db/app.db"

class Prod(Config):
    DEBUG = False

class Dev(Config):
    DEVELOPMENT = True
    DEBUG = True
