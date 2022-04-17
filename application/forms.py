from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SearchForm(FlaskForm):
    restaurant_name = StringField('Restaurant')
    cuisine = StringField('Cuisine')
    price_range = StringField('Price Range')
    submit = SubmitField('Search', render_kw={'class': 'btn btn-success btn-block'})


