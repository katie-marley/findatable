from application import db


class Restaurant(db.Model):
    Restaurant_ID = db.Column(db.Integer, primary_key=True)
    RestaurantName = db.Column(db.String(100), nullable=False)
    Address_Line_1 = db.Column(db.String(100), nullable=False)
    City = db.Column(db.String(50), nullable=False)
    Postcode = db.Column(db.String(12), nullable=False)
    Telephone = db.Column(db.String(20), nullable=False)
    Opening_Hours = db.Column(db.String(100), nullable=False)
    Cuisine = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.String(50), nullable=False)
    Image = db.Column(db.String(100), nullable=True)


# class Cuisine(db.Model):
#     Cuisine_ID = db.Column(db.Integer, primary_key=True)
#     Cuisine_Name = db.Column(db.String(50), nullable=False)


# class Price(db.Model):
#     Price_ID = db.Column(db.Integer, primary_key=True)
#     Price_Values = db.Column(db.String(50), nullable=False)

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


class Reservation(db.Model):
    Reservation_ID = db.Column(db.Integer, primary_key=True)
    Restaurant_ID = db.Column(db.Integer, db.ForeignKey('restaurant.Restaurant_ID'), nullable=False)
    User_ID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    RestaurantName = db.Column(db.String(50), nullable=False)
    reservation_date = db.Column(db.Date, nullable=False)
    reservation_time = db.Column(db.Time, nullable=False)
    party_size = db.Column(db.Integer, nullable=False)


class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    star_rating = db.Column(db.Integer, nullable=False)
    review_comment = db.Column(db.String(200), nullable=True)