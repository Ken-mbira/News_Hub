from . import news
from flask import render_template
from ..requests import get_sources  

@news.route('/')
def index():
    title = 'NEWS_HUB'
    sources = get_sources()
    return render_template('index.html',sources = sources, title = title) 