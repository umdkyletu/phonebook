from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

# define a blueprint for flask application
auth = Blueprint("auth", __name__)


# whenever you go to / the stuff in home def will happen/appear
@auth.route("/login", methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in sucessfully!', category='success')
                return redirect(url_for('views.contactlist'))
            else:
                flash('Incorrect password. Please try again.', category='error')
        else: 
            flash('Email does not exist.', category='error')
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<div></div>"


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered.', category='error')
        elif len(email) < 4:
            flash('Email must contain at least 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must contain at least 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must contain at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category= 'success')
            return redirect(url_for('views.contactlist'))


            
            
    return render_template("signUp.html")
