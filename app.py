from application import app
from flask import Flask, render_template
from wtform_field import *
# import the ./application/routes.py file
from application import routes


app.secret_key = 'replace later'


@app.route('/', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        return 'Great Success'
        # can then go on to change this to render the successful signup page #

    return render_template('signup.html', form=registration_form)


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)
