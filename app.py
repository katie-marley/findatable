from application import app
from flask import Flask, render_template
# import the ./application/routes.py file
from application import routes


app.secret_key = 'replace later'


@app.route('/', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)
