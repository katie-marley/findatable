from application import app
from flask import render_template, request
from application import app, db
from application.models import Users
from application import app
from flask import render_template
from application.wtform_field import *

app.secret_key = 'replace later'


@app.route('/', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data, password = form.password.data)        users = users(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Thank you!'

    return render_template('signup.html', form=form)
    # can then go on to change this to render the successful signup page #


if __name__ == '__main__':
    app.run(debug=True)
