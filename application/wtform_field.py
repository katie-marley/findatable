from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    """Registration Form"""

    username = StringField('username_label', validators=[InputRequired(message="Username Required"), Length(min=5, max=25, message="Username must be between 5 and 25 characters")])
    password = PasswordField('password_label',  validators=[InputRequired(message="Password Required"), Length(min=5, max=25, message="Password must be between 5 and 25 characters")])
    confirm_password = PasswordField('confirm_password_label',  validators=[InputRequired(message="Password Confirmation Required"), EqualTo('password', message="Passwords must match")])
    submit_button = SubmitField('Sign Up')