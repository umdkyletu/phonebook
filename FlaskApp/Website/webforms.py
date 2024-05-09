from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

#create a search form
class SearchForm(FlaskForm):
    """
    form used for searching contacts.
    
    Attr:
        - searched (stringField): field for entering search query.
        - submit (SubmitField): button for submitting search query.
    """
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")