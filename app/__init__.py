from flask import Flask
from .news import news,views
from config import config_options

def create_app(config_name):
    app = Flask(__name__)

    app.register_blueprint(news)
    app.config.from_object(config_options[config_name])

    return app