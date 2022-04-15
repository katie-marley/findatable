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
        PrefName = form.PrefName.data
        Password = form.Password.data
        Phone = form.Phone.data
        AddressLine1 = form.AddressLine1.data
        AddressLine2 = form.AddressLine2.data
        City = form.City.data
        Postcode = form.Postcode.data
        Allergens = form.Allergens.data

        if len(FirstName / LastName / Password / Phone / AddressLine1 / AddressLine2 / City / Postcode) == 0:
            error = "Please fill all necessary fields"
        else:
            user = User(FirstName=FirstName, LastName=LastName, PrefName=PrefName, Password=Password, Phone=Phone,
                        AddressLine1=AddressLine1, AddressLine2=AddressLine2, City=City, Postcode=Postcode,
                        Allergens=Allergens)
            db.session.add(user)
            db.session.commit()
            return 'Thank you!'

    return render_template('signup.html', form=form, message=error);
