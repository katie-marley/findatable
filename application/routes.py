import sqlalchemy
from flask import render_template, request
from application import app, db
from application.forms import SignUp
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

        Password = form.Password.data

        Phone = form.Phone.data

        AddressLine1 = form.AddressLine1.data

        if len(form.AddressLine2.data) == 0:
            AddressLine2 = sqlalchemy.null
        else:
            AddressLine2 = form.AddressLine2.data

        City = form.City.data

        Postcode = form.Postcode.data

        Allergens = form.Allergens.data

        if form.Password.data != form.ConfirmPassword.data:
            error = "Passwords must match"
        elif len(FirstName) == 0 or len(LastName) == 0 or len(Password) == 0 or len(AddressLine1) == 0 or len(AddressLine1) == 0 or len(City) == 0 or len(Postcode) == 0 or len(Allergens) == 0:
            error = "Please fill all necessary fields"
        else:
            user = User(FirstName=FirstName, LastName=LastName, PrefName=PrefName, Password=Password, Phone=Phone, AddressLine1=AddressLine1, AddressLine2=AddressLine2, City=City, Postcode=Postcode, Allergens=Allergens)
            db.session.add(user)
            db.session.commit()
            return render_template('signedup.html')

    return render_template('signup.html', form=form, message=error)
