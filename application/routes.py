import sqlalchemy
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask import render_template, request
from sqlalchemy.dialects import mysql

from application import app, db
from application.forms import SignUp, LogIn, LogOut
from application.models import User


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
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
        elif len(FirstName) == 0 or len(LastName) == 0 or len(Email) == 0 or len(Password) == 0 or len(AddressLine1) == 0 or len(AddressLine1) == 0 or len(City) == 0 or len(Postcode) == 0:
            error = "Please fill all necessary fields"
        else:
            user = User(FirstName=FirstName, LastName=LastName, PrefName=PrefName, Email=Email, Password=Password, Phone=Phone, AddressLine1=AddressLine1, AddressLine2=AddressLine2, City=City, Postcode=Postcode, Allergens=Allergens)
            db.session.add(user)
            db.session.commit()
            return render_template('signedup.html')

    return render_template('signup.html', form=form, message=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    form = LogIn()
    if request.method == 'POST':
        user_object = User.query.filter_by(Email=form.Email.data).first()
        real_password = user_object.Password

        if real_password == form.Password.data:
            session['id'] = user_object.id
            session['Preferred Name'] = user_object.PrefName
            session['Allergens'] = user_object.Allergens

            return render_template('loggedin.html')
        else:
            error = 'Invalid username or password'

    return render_template('login.html', form=form, message=error)


@app.route('/logout')
def logout():
    error = ''
    form = LogOut()
    return render_template('logout.html', form=form, message=error)