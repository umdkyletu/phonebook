from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Contact
from . import db
import json



# define a blueprint for flask application
views = Blueprint("views", __name__)


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

@views.route('/delete-contact',methods=['POST'])
def delete_contact():
    contact = json.loads(request.data)
    contactId = contact['contactId']
    contact = Contact.query.get(contactId)
    if contact:
        if contact.user_id == current_user.id:
            db.session.delete(contact)
            db.session.commit()
    
    return jsonify({})