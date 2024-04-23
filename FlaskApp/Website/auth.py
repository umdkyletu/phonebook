from flask import Blueprint, render_template, request, flash

# define a blueprint for flask application
auth = Blueprint("auth", __name__)


# whenever you go to / the stuff in home def will happen/appear
@auth.route("/login", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<div></div>"


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must contain at least 4 characters.', category='error')
        elif len(firstname) < 2:
            flash('First name must contain at least 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must contain at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
            
    return render_template("signUp.html")
