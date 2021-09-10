from flask import Flask
from .news import news,views

def create_app():
    app = Flask(__name__)

    app.register_blueprint(news)

    return app