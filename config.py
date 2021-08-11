import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCES_API_BASE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = '7d18ecd749d24ca3930cffe2f7a3c6cc'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}