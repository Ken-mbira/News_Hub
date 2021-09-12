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

def get_sources():
    """
    This will find the major headlines
    """
    get_headlines_url = BASE_URL.format('top-headlines/sources',NEWS_API)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headline_data = url.read()
        get_headline_response = json.loads(get_headline_data)['sources']
        result = process_sources(get_headline_response)
    return result

def process_sources(result_list):
    """
    Function that processes the results into the object with the properties we require
    
    Args: 
        result_list: This is the result after getting the url response
        
    Returns: A list of objects that only has the required properties
    """
    sources_list = []

    for source in result_list:
        id = source['id']
        name = source['name']
        description = source['description']
        category = source['category']
        country = source['country']

        new_source = Source(id,name,description,category,country)

        sources_list.append(new_source)

    return sources_list
