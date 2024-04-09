from flask import Blueprint

#define a blueprint for flask application
views = Blueprint('views',__name__)

#whenever you go to / the stuff in home def will happen/appear
@views.route('/')
def home():
    return "<h1>Test<h1>"