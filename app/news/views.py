from . import news
from flask import render_template,request,redirect,url_for
from ..requests import get_sources,get_articles  

@news.route('/')
def index():
    title = 'NEWS_HUB'
    sources = get_sources()
    covid = get_articles('covid')
    headlines = get_articles('popular')
    football = get_articles('football')

    search_article = request.args.get('article_search')

    # if search_article:
    #     return redirect(url_for('news.search',article_name = search_article))
    # else:
    return render_template('index.html',football = football,sources = sources, title = title, covid = covid,headlines = headlines) 

@news.route('/search/<article_name>')
def search(article_name):
    """
    This is the view function to display search results
    
    Args:
        article_name: This is the user inputted querry string
    Returns: A list of results matching the results
    """
    whole_article_name = article_name.split(" ")
    article_name_format = "+".join(whole_article_name)
    searched_results = get_articles(article_name_format)
    title = f'Search results for {article_name}'
    return render_template('search.html',articles = searched_results,title = title)
    