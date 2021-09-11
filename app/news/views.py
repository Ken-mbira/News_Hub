from . import news
from flask import render_template
# from ..requests import get_headlines  

@news.route('/')
def index():
    return render_template('index.html') 