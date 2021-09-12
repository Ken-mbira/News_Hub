from . import news
from flask import render_template
from ..requests import get_sources,get_articles  

@news.route('/')
def index():
    title = 'NEWS_HUB'
    sources = get_sources()
    covid = get_articles('covid')
    headlines = get_articles('politics')
    return render_template('index.html',sources = sources, title = title, covid = covid,headlines = headlines) 