import urllib.request,json

from .models import Source

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
        get_headline_response = json.loads(get_headline_data)

    return get_headline_response