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
    """
    renders an html template for the contact list page. if post is received, adds new contact to database.
    
    Returns:
        -  html code of contact list page.
    """
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
    """
    deletes a contact from the database.
    
    Returns:
        - dict: empty JSON response.
    """
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
    """
    updates an already existing contact in the database.
    
    Args:
        - id (int): id of contact that is to be updated.
        
    Returns:
        - redirect: redirects to contact page.
        - str: error message if a an error occurs while updating.
    """
    form = SearchForm()
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
        return render_template("update.html", contact=contact, user=current_user, form = form)



#search function
@views.route('/search', methods = ["POST"])
def search():
    """
    searches for contacts in database.
    
    Returns:
        - html template for search results page.
    """
    form = SearchForm()
    contacts = Contact.query
    if form.validate():
        searched = form.searched.data 
        contacts = contacts.filter(Contact.first_name.like('%' + searched + '%'))
        contacts = contacts.order_by(Contact.first_name).all()
        return render_template("search.html", form = form, searched = searched, contacts = contacts)
    
@views.context_processor
def inject_user():
    """
    injects the current for jinja templates.
    
    Returns:
        - dict: contains current user.
    """
    return dict(user=current_user)