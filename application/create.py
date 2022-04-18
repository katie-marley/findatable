# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

from application import db
from application.models import Restaurant, User, Cuisine, Price

db.drop_all()
db.create_all()


testPerson1 = User(FirstName='Julie', LastName='Dooley', PrefName='Jules', Email='JD@gmail.com', Password='password',
                    Phone='07763842259', AddressLine1='1', AddressLine2='The Hayes', City='Epsom', Postcode='KT186HB',
                    Allergens='None')

# inserting cuisine data #
cuisine1 = Cuisine(Cuisine_Name='Indian')
db.session.add(cuisine1)
cuisine2 = Cuisine(Cuisine_Name='Chinese')
db.session.add(cuisine2)
cuisine3 = Cuisine(Cuisine_Name='Italian')
db.session.add(cuisine3)
cuisine4 = Cuisine(Cuisine_Name='Lebanese')
db.session.add(cuisine4)
cuisine5 = Cuisine(Cuisine_Name='Japanese')
db.session.add(cuisine5)
cuisine6 = Cuisine(Cuisine_Name='Mexican')
db.session.add(cuisine6)

# inserting price points data
price1 = Price(Price_Values='£25 and under')
db.session.add(price1)
price2 = Price(Price_Values='£26 - £40')
db.session.add(price2)
price3 = Price(Price_Values='£41 and over')
db.session.add(price3)

# inserting test person
db.session.add(testPerson1)

# inserting restaurant data
restaurant1 = Restaurant(Restaurant_Name='The Famous Curry Bazaar', Address_Line_1='77 Brick Lane', City='London', Postcode='E1 6QL', Telephone='02073751986', Opening_Hours='Monday to Sunday, 12pm to 12am',Cuisine_ID=1, Price_ID=2)
db.session.add(restaurant1)
restaurant2 = Restaurant(Restaurant_Name='Orient London', Address_Line_1='15 Wardour Street', City='London', Postcode='W1D 6PH', Telephone='02079898880', Opening_Hours='Monday to Sunday, 11am to 11pm', Cuisine_ID=2, Price_ID=2)
db.session.add(restaurant2)
restaurant3 = Restaurant(Restaurant_Name='Pizza Hut', Address_Line_1='34 Colllege Raod', City='Harrow', Postcode='H1 1AT', Telephone='02088632525', Opening_Hours='Monday to Sunday, 11am to 6pm',Cuisine_ID=3, Price_ID=1)
db.session.add(restaurant3)
restaurant4 = Restaurant(Restaurant_Name='Tarboush', Address_Line_1='57 Market Street', City='Watford', Postcode='WD18 0PR', Telephone='01923248898', Opening_Hours='Monday to Sunday, 11am to 12am', Cuisine_ID=4, Price_ID=1)
db.session.add(restaurant4)
restaurant5 = Restaurant(Restaurant_Name='Umu Restaurant', Address_Line_1='14 to 16 Bruton Place', City='London', Postcode='W1 6LX', Telephone='02074998881', Opening_Hours='Monday to Sunday, 12pm to 2 pm, 6pm to 10pm', Cuisine_ID=5, Price_ID=3)
db.session.add(restaurant5)
restaurant6 = Restaurant(Restaurant_Name='Ella Canta', Address_Line_1='1 Hambleton Place', City='London', Postcode='W1J 7QI', Telephone='02073188715', Opening_Hours='Monday to Sunday, 12pm to 12am', Cuisine_ID=6, Price_ID=3)
db.session.add(restaurant6)
restaurant7 = Restaurant(Restaurant_Name='Wahaca Covent Garden', Address_Line_1='66 Chandos Place', City='London', Postcode='WC2N 4HG', Telephone='020 3951 9741', Opening_Hours='Monday to Sunday, 12pm to 10pm', Cuisine_ID= 6, Price_ID=2)
db.session.add(restaurant7)

db.session.commit()
