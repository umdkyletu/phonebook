from flask import Blueprint, render_template

# define a blueprint for flask application
auth = Blueprint("auth", __name__)


# whenever you go to / the stuff in home def will happen/appear
@auth.route("/login")
def login():
    # functions for logging in would go in here
    return render_template("login.html")


@auth.route("/logout")
def logout():
    # functions for logging out would go in here
    return "<div></div>"


@auth.route("/signup")
def signup():
    # functions for signing in would go in here
    return render_template("signUp.html")
