from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, EqualTo, Length
from wtforms import StringField, SubmitField, IntegerField, DateField, TimeField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired, EqualTo, Length, DataRequired


# class SearchForm(FlaskForm):
#     restaurant_name = StringField('Restaurant')
#     cuisine = StringField('Cuisine')
#     price_range = StringField('Price Range')
#     submit = SubmitField('Search', render_kw={'class': 'btn btn-success btn-block'})


class SignUp(FlaskForm):
    FirstName = StringField('First Name', validators=[InputRequired(), Length(min=1, max=50)])
    LastName = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=50)])
    PrefName = StringField('Preferred Name')
    Email = StringField('Email', validators=[InputRequired()])
    Password = StringField('Password',
                           validators=[InputRequired(), EqualTo('ConfirmPassword', message='Passwords must match'),
                                       Length(min=5, max=50)])
    ConfirmPassword = StringField('Confirm Password')
    Phone = IntegerField('Phone', validators=[InputRequired()])
    AddressLine1 = StringField('Address Line 1', validators=[InputRequired()])
    AddressLine2 = StringField('Address Line 2')
    City = StringField('City', validators=[InputRequired()])
    Postcode = StringField('Postcode', validators=[InputRequired(), Length(min=4, max=7, message='Invalid Postcode')])
    Allergens = StringField('Allergens')
    submit = SubmitField('Sign Up')
    # add an input for cars info #


class LogIn(FlaskForm):
    Email = StringField('Email', validators=[InputRequired()])
    Password = StringField('Password', validators=[InputRequired()])
    login_button = SubmitField('Log In')
    signup_button = SubmitField('Sign Up')
    # add an input for cars info #


# RESTAURANT PAGE
class ReservationForm(FlaskForm):
    reservation_date = DateField('Date:', validators=[DataRequired()])
    reservation_time = TimeField('Time:', validators=[DataRequired()])
    party_size = IntegerField('Party Size:', validators=[DataRequired()])
    submit1 = SubmitField('Submit Booking!')


# ACCOUNT PAGE
class ReviewsForm(FlaskForm):
    star_rating = RadioField('Rating',
                             choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')],
                             validators=[DataRequired()])
    review_comment = TextAreaField('Tell us what you think:')
    submit2 = SubmitField('Submit Review!')


class Search(FlaskForm):
    dropdown_cuisine = ['None chosen', 'Italian', 'Chinese', 'Indian', 'Mexican', 'Lebanese']
    dropdown_price = ['None chosen', '£25 and under', '£26 - £40', '£41 and over']
    Cuisine = SelectField('Food Types', choices=dropdown_cuisine, default=1)
    Price = SelectField('Prices Types', choices=dropdown_price, default=1)
    search_button = SubmitField('Search')