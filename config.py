def determine_env(app):
    if app.config['ENV'] == 'development':
        return 'config.DevelopmentConfig'
    elif app.config['ENV'] == 'homologation':
        return 'config.HomologationConfig'
    elif app.config['ENV'] == 'production':
        return 'config.ProductionConfig'


class Config(object):
    DEBUG = False
    TESTING = False
    LOCAL = True
    MONGO_URI = 'mongodb://localhost:27017/register'
    MONGO_DBNAME = 'register'
    MONGO_USERNAME = 'username'
    MONGO_PASSWORD = 'password'


class ProductionConfig(Config):
    LOCAL = False
    MONGO_URI = 'mongodb://localhost:27017/register'
    MONGO_DBNAME = 'register'
    MONGO_USERNAME = 'username'
    MONGO_PASSWORD = 'password'


class HomologationConfig(Config):
    LOCAL = False
    MONGO_URI = 'mongodb://192.168.10.132:27017/register'
    MONGO_DBNAME = 'register'
    MONGO_USERNAME = 'username'
    MONGO_PASSWORD = 'password'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    pass
