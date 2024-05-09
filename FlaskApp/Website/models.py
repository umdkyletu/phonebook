from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Contact(db.Model):
    """
    Represents contact in database.
    
    Attr:
        - id (int): primary key
        - first_name (str): first name 
        - last_name (str): last name
        - number (str): phone number
        - photo (str): url of photo representing contact
        - date (DateTime): date and time when contact was added
        - user_id (int):  foreign key referencing id of user who owns contact
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    number = db.Column(db.String(150))
    photo = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    """
    represents user in database.
    
    Attr:
        - id (int): primary id
        - email (str) email address
        - password (str): password
        - first_name (str): first name
        - contacts (relationship): one-to-many rel with contact model
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    contacts = db.relationship("Contact")
