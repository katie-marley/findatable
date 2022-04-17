# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

from application import db
from models import Restaurant

restaurant18 = Restaurant(Restaurant_Name='Wahaca Covent Garden', Address_Line_1='66 Chandos Place', City='London', Postcode='WC2N 4HG', Telephone='020 3951 9741', Opening_Hours='Monday to Sunday, 12pm to 10pm',Cuisine_ID=6, Price_ID=2)


restaurant = [restaurant18]
db.session.add(restaurant18)
db.session.commit()