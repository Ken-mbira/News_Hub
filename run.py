from app import create_app
from app.requests import get_headlines

myApp = create_app('development')
print(get_headlines())

if __name__ == '__main__':
    myApp.run()