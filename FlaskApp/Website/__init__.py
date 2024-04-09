from flask import Flask

def create_app():
    #creates flask app
    app = Flask(__name__)
    #encrypts cookies and session data
    app.config['SECRET_KEY'] = 'fhdgwefgifuejukf'

    from .views import views
    from .auth import auth

    #register blueprints with flask app and set url prefix to be / which means no prefix for the route
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
