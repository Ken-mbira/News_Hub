import os

class Config:
    """
    This is the parent configuration class that contains the main configurations that are to work on the application
    """
    NEWS_API = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    BASE_URL = 'https://newsapi.org/v2/{}?q={}&apiKey={}'

class ProdConfig(Config):
    """
    This is the child of config class and contains confugurations to used in production
    """
    pass

class DevConfig(Config):
    """
    This is a child of config class and contains configurations for the development
    """
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}