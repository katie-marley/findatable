from application import app
# import the ./application/routes.py file
from application import routes

# comment added #
if __name__ == '__main__':
     # app.run(debug=True, host='0.0.0.0')
     app.run(debug=True)