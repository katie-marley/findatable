from application import db
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
