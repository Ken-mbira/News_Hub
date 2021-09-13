## NEWS HUB
This is a web application that displays news articles from multiple sources to a user. It consumes the NEWS API to get all the requests.

# Contributors
1. Ken Mbira

# Technologies Used
1. Flask
2. HTML
3. CSS
4. Bootstrap
5. Python
6. Javascipt

# Dependencies
For full functionality of the application install the following:

certifi==2021.5.30
charset-normalizer==2.0.4
click==8.0.1
dominate==2.6.0
Flask==2.0.1
Flask-Bootstrap==3.3.7.1
Flask-Script==2.0.6
gunicorn==20.1.0
idna==3.2
itsdangerous==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1
requests==2.26.0
urllib3==1.26.6
visitor==0.1.3
Werkzeug==2.0.1

# Set Up Instructions
To have the repo locally on your machine:
1. Create a designated repo location and then using the terminal type 'git clone' followed by the link of the  repo

# App Description
The application consumes the NEWS_API to get news from a variety of news sources and according to queries that are passed in via the views.py file, filters the data and brings back only the specified data. This application shows different categories of news on the home page and has a functionality where the user can search for a specific area of interest in which case they are redirected to the search page where they view their results in a list of cards

# Link to live site
To view the deployed application click [here](https://news-galore.herokuapp.com/)

# Known Bugs
The application has been deployed to heroku but is currently not functional. I am still working out the reason for this. Feel free to point out the error if you can see it from your side.

# Future Improvements
In the future I would like to implements a subscription functionality where a user can have an account and by doing so have special features in their application.

# Contact Information
1. Phone: 0758926990
2. email: mbiraken17gmail.com
3. Twitter: Ken Mbira
4. Linkedin: Ken Mbira
5. Git-hub: Ken-mbira

# License Information
MIT License

Copyright (c) [2021] [Ken-mbira]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
