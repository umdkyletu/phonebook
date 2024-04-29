from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Contact
from . import db


# define a blueprint for flask application
views = Blueprint("views", __name__)


# whenever you go to / the stuff in home def will happen/appear
# @views.route("/")
# @login_required
# def home():
#     return render_template("base.html")

@views.route("/",methods=['GET', 'POST'])
@login_required
def contactlist():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        number = request.form.get('number')
        if len(first_name) < 2:
            flash('First name must contain at least 2 characters.', category='error')
        if len(last_name) < 2:
            flash('First name must contain at least 2 characters.', category='error')
        else:
            new_contact = Contact(first_name = first_name, last_name=last_name, number=number, user_id = current_user.id)
            db.session.add(new_contact)
            db.session.commit()
            flash("Contact Added", category= 'success')
            
    return render_template("contactlist.html", user = current_user)