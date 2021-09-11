from app import create_app

myApp = create_app('development')

if __name__ == '__main__':
    myApp.run()