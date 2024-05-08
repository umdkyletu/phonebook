from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Contact
from .webforms import SearchForm
from . import db
import json


# define a blueprint for flask application
views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def contactlist():
    form = SearchForm()
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        number = request.form.get("number")
        photo = request.form.get("photo")
        if len(first_name) < 2:
            flash("First name must contain at least 2 characters.", category="error")
        if len(last_name) < 2:
            flash("First name must contain at least 2 characters.", category="error")
        else:
            new_contact = Contact(
                first_name=first_name,
                last_name=last_name,
                number=number,
                user_id=current_user.id,
                photo=photo,
            )
            db.session.add(new_contact)
            db.session.commit()
            flash("Contact Added", category="success")

    return render_template("contactlist.html", user=current_user, form=form)


@views.route("/delete-contact", methods=["POST"])
def delete_contact():
    contact = json.loads(request.data)
    contactId = contact["contactId"]
    contact = Contact.query.get(contactId)
    if contact:
        if contact.user_id == current_user.id:
            db.session.delete(contact)
            db.session.commit()

    return jsonify({})


@views.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    contact = Contact.query.get(id)
    if request.method == "POST":
        contact.first_name = request.form.get("first_name")
        contact.last_name = request.form.get("last_name")
        contact.number = request.form.get("number")
        contact.photo = request.form.get("photo")
        print("First Name:", contact.first_name)
        print("Last Name:", contact.last_name)
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was a problem updating"
    else:
        return render_template("update.html", contact=contact, user=current_user)



#search function
@views.route('/search', methods = ["POST"])
def search():
    form = SearchForm()
    contacts = Contact.query
    if form.validate():
        searched = form.searched.data 
        contacts = contacts.filter(Contact.first_name.like('%' + searched + '%'))
        contacts = contacts.order_by(Contact.first_name).all()
        return render_template("search.html", form = form, searched = searched, contacts = contacts)
    
@views.context_processor
def inject_user():
    return dict(user=current_user)