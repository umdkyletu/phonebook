from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from flask_login import login_required, logout_user, current_user, login_user


# define a blueprint for flask application
auth = Blueprint("auth", __name__)

# whenever you go to / the stuff in home def will happen/appear
@auth.route("/login", methods=['GET', 'POST'])
def login():
    """
    renders login page.
    
    Returns:
        - rendered html template for login page.
        - redirect: redirects to contact list page if login successful.
    """    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in sucessfully!', category='success')
                login_user(user, remember = True)
                return redirect(url_for('views.contactlist'))
            else:
                flash('Incorrect password. Please try again.', category='error')
        else: 
            flash('Email does not exist.', category='error')
    return render_template("login.html", user= current_user)


@auth.route("/logout")
@login_required
def logout():
    """
    logs out user.
    
    Returns:
        - redirect: redirects to login page.
        
    """
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    """
    renders signup page.
    
    Returns:
        - rendered html template for signup page.
        - redirect: redirects to contact list page if signup successful.
    """
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
            login_user(new_user, remember = True)
            flash("Account created!", category= 'success')
            return redirect(url_for('views.contactlist'))
        
    return render_template("signUp.html", user= current_user)
