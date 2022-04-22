from datetime import datetime

from application import db


class Restaurant(db.Model):
    Restaurant_ID = db.Column(db.Integer, primary_key=True)
    Restaurant_Name = db.Column(db.String(50), nullable=False)
    Address_Line_1 = db.Column(db.String(50), nullable=False)
    City = db.Column(db.String(50), nullable=False)
    Postcode = db.Column(db.String(8), nullable=False)
    Telephone = db.Column(db.String(15), nullable=False)
    Opening_Hours = db.Column(db.String(50), nullable=False)
    Cuisine_ID = db.Column(db.Integer, db.ForeignKey('cuisine.Cuisine_ID'), nullable=False)
    Price_ID = db.Column(db.Integer, db.ForeignKey('price.Price_ID'), nullable=False)


class Cuisine(db.Model):
    Cuisine_ID = db.Column(db.Integer, primary_key=True)
    Cuisine_Name = db.Column(db.String(50), nullable=False)


class Price(db.Model):
    Price_ID = db.Column(db.Integer, primary_key=True)
    Price_Values = db.Column(db.String(50), nullable=False)


# import the sqlalchemy object (db) created for our app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(30), nullable=False)
    LastName = db.Column(db.String(30), nullable=False)
    PrefName = db.Column(db.String(30), nullable=True)
    Email = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(30), nullable=False)
    Phone = db.Column(db.String(30), nullable=False)
    AddressLine1 = db.Column(db.String(30), nullable=False)
    AddressLine2 = db.Column(db.String(30), nullable=True)
    City = db.Column(db.String(30), nullable=False)
    Postcode = db.Column(db.String(30), nullable=False)
    Allergens = db.Column(db.String(100), nullable=False)
    # cars = db.relationship('Car', backref='person')
    # user can have many reviews
    reviews = db.relationship('Reviews', backref='reviewer')


class Reservation(db.Model):
    Reservation_ID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reservation_date = db.Column(db.Date, nullable=False)
    reservation_time = db.Column(db.Time, nullable=False)
    party_size = db.Column(db.Integer, nullable=False)


class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    # author = db.Column(db.String(255))
    star_rating = db.Column(db.Integer, nullable=False)
    review_comment = db.Column(db.Text, nullable=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    # Foriegn Key to link users(refer to the primary key of the user
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id'))

