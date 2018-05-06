class Config(object):
    '''Base config class.'''
    pass

class ProConfig(Config):
    '''Production config class.'''
    pass

class DevConfig(Config):
    '''Development config class.'''
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:ADDR66@127.0.0.1:3306/lightblog'