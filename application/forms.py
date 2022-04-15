from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SignUp(FlaskForm):
    FirstName = StringField('First Name')
    LastName = StringField('Last Name')
    PrefName = StringField('Preferred Name')
    Password = StringField('Password')
    Phone = StringField('Phone')
    AddressLine1 = StringField('Address Line 1')
    AddressLine2 = StringField('Address Line 2')
    City = StringField('City')
    Postcode = StringField('Postcode')
    Allergens = StringField('Allergens')
    submit = SubmitField('Sign Up')
    # add an input for cars info #


