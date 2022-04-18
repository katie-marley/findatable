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
