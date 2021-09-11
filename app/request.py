import urllib.request,json

NEWS_API = None

def configure_request(app):
    """
    This function will take in an application instance and replace the None variables with configuration objects
    
    Args:
        app: This is the application instance that will be taken in
    """
    global NEWS_API
    NEWS_API = app.config['NEWS_API_KEY']