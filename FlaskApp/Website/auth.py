from flask import Blueprint

#define a blueprint for flask application
auth = Blueprint('auth',__name__)

#whenever you go to / the stuff in home def will happen/appear
@auth.route('/login')
def login():
    #functions for logging in would go in here
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    #functions for logging out would go in here
    return "<p>logout</p>"

@auth.route('/signup')
def signup():
    #functions for signing in would go in here
    return "<p>signup</p>"