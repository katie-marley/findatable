from flask import render_template, request
from application import app, db
from application.forms import SearchForm
from application.models import Restaurant
from application.models import Price
from application.models import Cuisine




@app.route('/', methods=['GET','POST'])
def home_search():
    form = SearchForm()
    return render_template('home_search.html', form=form)




@app.route('/results', methods= ['GET', 'POST'])
def hello():
    rest = Restaurant.query.all()
    print(rest)
    return render_template('search_results.html', rest=rest)







#  @app.route('/search_results', methods=['GET'])