from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, EqualTo, Length


class SignUp(FlaskForm):
    FirstName = StringField('First Name', validators=[InputRequired(), Length(min=1, max=50)])
    LastName = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=50)])
    PrefName = StringField('Preferred Name')
    Password = StringField('Password', validators=[InputRequired(), EqualTo('ConfirmPassword', message='Passwords must match'), Length(min=5, max=50)])
    ConfirmPassword = StringField('Confirm Password')
    Phone = IntegerField('Phone', validators=[InputRequired()])
    AddressLine1 = StringField('Address Line 1', validators=[InputRequired()])
    AddressLine2 = StringField('Address Line 2')
    City = StringField('City', validators=[InputRequired()])
    Postcode = StringField('Postcode', validators=[InputRequired(), Length(min=4, max=7, message='Invalid Postcode')])
    Allergens = StringField('Allergens', validators=[InputRequired()])
    submit = SubmitField('Sign Up')
    # add an input for cars info #


