from os import name
from test_source import SourceTest
import urllib.request,json

from .models import Source,Article

NEWS_API = None
BASE_URL = None

def configure_request(app):
    """
    This function will take in an application instance and replace the None variables with configuration objects
    
    Args:
        app: This is the application instance that will be taken in
    """
    global NEWS_API,BASE_URL
    NEWS_API = app.config['NEWS_API']
    BASE_URL = app.config['BASE_URL']

def get_headlines():
    """
    This will find the major headlines
    """
    get_headlines_url = BASE_URL.format('top-headlines',NEWS_API)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headline_data = url.read()
        get_headline_response = json.loads(get_headline_data)['articles']
        result = process_articles(get_headline_response)
    return result

def process_articles(result_list):
    """
    Function that processes the results into the object with the properties we require
    
    Args: 
        result_list: This is the result after getting the url response
        
    Returns: A list of objects that only has the required properties
    """
    articles_list = []
    for article in result_list:
        source = article['source']['name']
        author = article['author']
        title = article['title']
        description = article['description']
        link = article['url']
        image_url = article['urlToImage']
        published = article['publishedAt']
        
        new_article = Article(source,author,title,description,link,image_url,published)

        articles_list.append(new_article)

    return articles_list