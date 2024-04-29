from flask import Blueprint, render_template
from flask_login import login_required, logout_user, current_user, login_user


# define a blueprint for flask application
views = Blueprint("views", __name__)


# whenever you go to / the stuff in home def will happen/appear
# @views.route("/")
# @login_required
# def home():
#     return render_template("base.html")

@views.route("/")
@login_required
def contactlist():
    return render_template("contactlist.html")