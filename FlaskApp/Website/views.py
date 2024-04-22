from flask import Blueprint, render_template

# define a blueprint for flask application
views = Blueprint("views", __name__)


# whenever you go to / the stuff in home def will happen/appear
@views.route("/")
def home():
    return render_template("base.html")