#  @app.route('/search_results', methods=['GET'])
import sqlalchemy
from flask import Flask, render_template, request, redirect, url_for, session, flash, sessions
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask import render_template, request
from sqlalchemy.dialects import mysql
from sqlalchemy.sql.functions import current_user

from application import app, db
from application.forms import SignUp, LogIn
from application.models import User, Reviews
from flask import render_template, request
from application import app, db
from application.forms import SearchForm, ReviewsForm, ReservationForm
from application.models import Restaurant, Reservation
from application.models import Price
from application.models import Cuisine


@app.route('/search', methods=['GET', 'POST'])
def home_search():
    form = SearchForm()
    return render_template('home_search.html', form=form)


@app.route('/results', methods=['GET', 'POST'])
def hello():
    rest = Restaurant.query.all()
    print(rest)
    return render_template('search_results.html', rest=rest)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    form = SignUp()

    if request.method == 'POST':
        FirstName = form.FirstName.data
        LastName = form.LastName.data

        if len(form.PrefName.data) == 0:
            PrefName = FirstName
        else:
            PrefName = form.PrefName.data

        Email = form.Email.data
        Password = form.Password.data
        Phone = form.Phone.data
        AddressLine1 = form.AddressLine1.data

        if len(form.AddressLine2.data) == 0:
            AddressLine2 = 'None Given'
        else:
            AddressLine2 = form.AddressLine2.data

        City = form.City.data
        Postcode = form.Postcode.data

        if len(form.Allergens.data) == 0:
            Allergens = 'None Given'
        else:
            Allergens = form.Allergens.data

        user_object = User.query.filter_by(Email=Email).first()
        if user_object:
            error = "This email has already been used"

        elif form.Password.data != form.ConfirmPassword.data:
            error = "Passwords must match"
        elif len(FirstName) == 0 or len(LastName) == 0 or len(Email) == 0 or len(Password) == 0 or len(
                AddressLine1) == 0 or len(AddressLine1) == 0 or len(City) == 0 or len(Postcode) == 0:
            error = "Please fill all necessary fields"
        else:
            user = User(FirstName=FirstName, LastName=LastName, PrefName=PrefName, Email=Email, Password=Password,
                        Phone=Phone, AddressLine1=AddressLine1, AddressLine2=AddressLine2, City=City, Postcode=Postcode,
                        Allergens=Allergens)
            db.session.add(user)
            db.session.commit()
            return render_template('signedup.html')

    return render_template('signup.html', form=form, message=error)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    form = LogIn()
    session['id'] = None
    session['Preferred Name'] = None
    session['Allergens'] = None

    if request.method == 'POST':

        user_object = User.query.filter_by(Email=form.Email.data).first()
        if user_object:
            real_password = user_object.Password

            if real_password == form.Password.data:
                session['id'] = user_object.id
                session['Preferred Name'] = user_object.PrefName
                session['Allergens'] = user_object.Allergens

                return render_template('home_search.html')
            else:
                error = 'Invalid username or password'
        else:
            error = 'Invalid username or password'

    return render_template('login.html', form=form, message=error)


# Restaurant page roots
@app.route('/restaurant_page/', methods=['GET', 'POST'])
def make_reservation():
    form = ReservationForm()
    reviews = Reviews.query.order_by(Reviews.date_posted)
    # reviews_form = ReviewsForm

    if request.method == 'POST':
        # fetch and store data
        reservation_date = form.reservation_date.data
        reservation_time = form.reservation_time.data
        party_size = form.party_size.data

        reservation = Reservation(reservation_date=reservation_date, reservation_time=reservation_time,
                                  party_size=party_size)
        db.session.add(reservation)
        db.session.commit()
        return 'Booking Confirmed!'

    return render_template('restaurant_page.html', form=form, reviews=reviews)


@app.route('/account/', methods=['GET', 'POST'])
def submit_review():
    form = ReviewsForm()

    if request.method == 'POST':
        star_rating = form.star_rating.data
        review_comment = form.review_comment.data
        reviewer = Reviews.reviewer_id

        # reviewer =
        review = Reviews(star_rating=star_rating, reviewer_id=reviewer, review_comment=review_comment)

        # add review to database
        db.session.add(review)
        db.session.commit()

        # clear the form
        form.star_rating.data = " "
        form.review_comment.data = " "

        # return a message
        flash("Review Submitted!")

    return render_template('account.html', form=form)


# @app.route('/reviewspage/', methods=['GET', 'POST'])
# def display_review():
# form = ReviewsForm()
# reviews = Reviews.query.order_by(Reviews.date_posted)
# return render_template('reviewspage.html', form=form, reviews=reviews)


@app.route('/restaurantpage/')
def display_review2():
    form = ReservationForm()
    reviews = Reviews.query.order_by(Reviews.date_posted)
    return render_template('restaurant_page.html', form=form, reviews=reviews)


@app.route('/booking/')
def display_reservation():
    form = ReviewsForm
    bookings = Reservation.query.all()
    return render_template('account.html', form=form, bookings=bookings)
