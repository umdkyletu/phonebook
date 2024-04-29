from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

DB_NAME = "database.db"
def create_app():
    #creates flask app
    app = Flask(__name__)
    #encrypts cookies and session data
    app.config['SECRET_KEY'] = 'fhdgwefgifuejukf'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    #register blueprints with flask app and set url prefix to be / which means no prefix for the route
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Contact

    create_database(app)

    return app


def create_database(app):
    with app.app_context():
        if not path.exists('Website/' + DB_NAME):
            db.create_all()
            print('Created Database!')
