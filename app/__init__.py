from flask_bootstrap import Bootstrap

from app.requests import configure_request
from flask import Flask
from .news import news,views
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    bootstrap.init_app(app)
    
    app.register_blueprint(news)
    app.config.from_object(config_options[config_name])
    configure_request(app)

    return app