from flask import render_template
from . import news

@news.app_errorhandler(404)
def fourOfour(error):
    """
    Function to display the error page
    """
    render_template('fourOfour.html'),404