from flask_bootstrap import Bootstrap

from app.requests import configure_request
from flask import Flask
from .news import news,views,error
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    app.register_blueprint(news)
    app.config.from_object(config_options[config_name])
    configure_request(app)

    bootstrap.init_app(app)

    return app