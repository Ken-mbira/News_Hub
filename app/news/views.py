from . import news
from flask import render_template
from ..requests import get_headlines  

@news.route('/')
def index():
    title = 'NEWS_HUB'
    articles = get_headlines()
    return render_template('index.html',articles = articles, title = title) 