from . import news
from flask import render_template

@news.route('/')
def index():
    return render_template('index.html') 