class Config(object):
    '''Base config class.'''
    SECRET_KEY = '6\xba\xcc\x99\xf4\xe1\x01\xddLy7\xf2N]\t\x81\x83x\xce\xbb\xb6z\xeb\xdf'

class ProConfig(Config):
    '''Production config class.'''
    pass

class DevConfig(Config):
    '''Development config class.'''
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:ADDR66@127.0.0.1:3306/lightblog'