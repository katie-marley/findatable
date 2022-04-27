# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

from application import db
from application.models import Restaurant, User

db.drop_all()
db.create_all()


testPerson1 = User(FirstName='Julie', LastName='Dooley', PrefName='Jules', Email='JD@gmail.com', Password='password',
                    Phone='07763842259', AddressLine1='1', AddressLine2='The Hayes', City='Epsom', Postcode='KT186HB',
                    Allergens='None')

# # inserting cuisine data #
# cuisine1 = Cuisine(Cuisine='Indian')
# db.session.add(cuisine1)
# cuisine2 = Cuisine(Cuisine='Chinese')
# db.session.add(cuisine2)
# cuisine3 = Cuisine(Cuisine_Name='Italian')
# db.session.add(cuisine3)
# cuisine4 = Cuisine(Cuisine_Name='Lebanese')
# db.session.add(cuisine4)
# cuisine5 = Cuisine(Cuisine_Name='Japanese')
# db.session.add(cuisine5)
# cuisine6 = Cuisine(Cuisine_Name='Mexican')
# db.session.add(cuisine6)

# # inserting price points data
# price1 = Price(Price_Values='£25 and under')
# db.session.add(price1)
# price2 = Price(Price_Values='£26 - £40')
# db.session.add(price2)
# price3 = Price(Price_Values='£41 and over')
# db.session.add(price3)

# inserting test person
db.session.add(testPerson1)
db.session.commit()

# inserting restaurant data
restaurant1 = Restaurant(RestaurantName='The Famous Curry Bazaar', Address_Line_1='77 Brick Lane', City='London', Postcode='E1 6QL', Telephone='020 7375 1986', Opening_Hours='Monday - Sunday: 12pm - 12am',Cuisine='Indian', Price='£26 - £40', Image='curry_bazaar_logo.png')
db.session.add(restaurant1)
db.session.commit()
restaurant2 = Restaurant(RestaurantName='Orient London', Address_Line_1='15 Wardour Street', City='London', Postcode='W1D 6PH', Telephone='020 7989 8880', Opening_Hours='Monday - Sunday: 11am - 11pm', Cuisine='Chinese', Price='£26 - £40', Image='orient_logo.png')
db.session.add(restaurant2)
db.session.commit()
#  restaurant3 = Restaurant(RestaurantName='Pizza Hut', Address_Line_1='34 Colllege Raod', City='Harrow', Postcode='H1 1AT', Telephone='02088632525', Opening_Hours='Monday to Sunday, 11am to 6pm',Cuisine='Italian', Price='£25 and under')
#  db.session.add(restaurant3)
restaurant4 = Restaurant(RestaurantName='Tarboush', Address_Line_1='57 Market Street', City='Watford', Postcode='WD18 0PR', Telephone='01923 248 898', Opening_Hours='Monday - Sunday: 11am - 12am', Cuisine='Lebanese', Price='£25 & under', Image='tarboush_logo.png')
db.session.add(restaurant4)
db.session.commit()
restaurant5 = Restaurant(RestaurantName='Umu Restaurant', Address_Line_1='14-16 Bruton Place', City='London', Postcode='W1 6LX', Telephone='020 7499 8881', Opening_Hours='Monday - Sunday: 12pm - 2 pm & 6pm - 10pm', Cuisine='Japanese', Price='£41 & over', Image='umu_logo.jpg')
db.session.add(restaurant5)
db.session.commit()
restaurant6 = Restaurant(RestaurantName='Ella Canta', Address_Line_1='1 Hambleton Place', City='London', Postcode='W1J 7QI', Telephone='020 7318 8715', Opening_Hours='Monday - Sunday: 12pm - 12am', Cuisine='Mexican', Price='£41 & over', Image='ella_canta_logo.png')
db.session.add(restaurant6)
db.session.commit()
restaurant7 = Restaurant(RestaurantName='Wahaca Covent Garden', Address_Line_1='66 Chandos Place', City='London', Postcode='WC2N 4HG', Telephone='020 3951 9741', Opening_Hours='Monday - Sunday: 12pm - 10pm', Cuisine='Mexican', Price='£26 - £40', Image='wahaca_logo.png')
db.session.add(restaurant7)
db.session.commit()
restaurant8 = Restaurant(RestaurantName='Benares Restaurant Mayfair', Address_Line_1='12a Berkeley Square', City='London', Postcode='W1J 6BS', Telephone='020 7629 8886', Opening_Hours='Monday - Saturday: 12.30pm - 2.30pm & 5.30pm - 10.30pm', Cuisine='Indian', Price='£41 & over', Image='benares_logo.png')
db.session.add(restaurant8)
db.session.commit()
restaurant9 = Restaurant(RestaurantName='Brigadiers', Address_Line_1='1-5 Bloomberg Arcade', City='London', Postcode='EC4N 8AR', Telephone='020 3319 8140', Opening_Hours='Monday - Saturday: 12.30pm - 2.45pm & 5.00pm - 10.45pm', Cuisine='Indian', Price='£25 & under', Image='brigadiers_logo.png')
db.session.add(restaurant9)
db.session.commit()
restaurant10 = Restaurant(RestaurantName='Miyako', Address_Line_1='40 Liverpool Street', City='London', Postcode='EC2M 7QN', Telephone='020 7618 7100', Opening_Hours='Monday - Friday: 12.00pm - 3.00pm & 5.00pm - 10.00pm', Cuisine='Japanese', Price='£25 & under', Image='miyako_logo.jpg')
db.session.add(restaurant10)
db.session.commit()
restaurant11 = Restaurant(RestaurantName='Moshi Moshi Sushi', Address_Line_1='24 Liverpool Street', City='London', Postcode='EC2M 7QH', Telephone='020 7247 3227', Opening_Hours='Tuesday - Friday: 11.30am - 9pm', Cuisine='Japanese', Price='£26 - £40', Image='moshi_logo.jpg')
db.session.add(restaurant11)
db.session.commit()
restaurant12 = Restaurant(RestaurantName='Kai Mayfair', Address_Line_1='65 South Audley Street', City='London', Postcode='W1K 2QU', Telephone='020 7493 8988', Opening_Hours='Monday - Sunday: 12pm - 11pm', Cuisine='Chinese', Price='£41 & over', Image='kai_logo.jpg')
db.session.add(restaurant12)
db.session.commit()
restaurant13 = Restaurant(RestaurantName='Royal China London', Address_Line_1='30 Westferry Circus', City='London', Postcode='E14 8RR', Telephone='020 7719 0888', Opening_Hours='Monday - Sunday: 12pm - 10pm', Cuisine='Chinese', Price='£25 & under', Image='royal_china_logo.png' )
db.session.add(restaurant13)
db.session.commit()
restaurant14 = Restaurant(RestaurantName='Locanda Locatelli', Address_Line_1='8 Seymour Street', City='London', Postcode='W1H 7JZ', Telephone='020 7935 9088', Opening_Hours='Wednesday - Sunday: 12pm - 3pm & 6pm - 11pm', Cuisine='Italian', Price='£41 & over', Image='locanda_logo.png')
db.session.add(restaurant14)
db.session.commit()
restaurant15 = Restaurant(RestaurantName='Bancone', Address_Line_1='39 William IV Street', City='London', Postcode='WC2N 4DD' , Telephone='020 7240 8786', Opening_Hours='Monday - Sunday: 12pm - 3pm & 5pm - 9.30pm', Cuisine='Italian', Price='£25 & under', Image='bancone_logo.png')
db.session.add(restaurant15)
db.session.commit()
restaurant16 = Restaurant(RestaurantName='Ristorante Frescobaldi London', Address_Line_1='15 New Burlington Place', City='London', Postcode='W1S 2HX', Telephone='020 3693 3435', Opening_Hours='Monday - Saturday: 12pm - 3pm & 5pm - 11pm', Cuisine='Italian', Price='£26 - £40', Image='frescobaldi_logo.jpg')
db.session.add(restaurant16)
db.session.commit()
restaurant17 = Restaurant(RestaurantName='Ishbilia Lebanese Restaurant', Address_Line_1='8-9 William Street', City='London', Postcode='SW1X 9HL', Telephone='020 7235 7788', Opening_Hours='Monday - Saturday: 12pm - 2am', Cuisine='Lebanese', Price='£41 & over', Image='ishbilia_logo.png')
db.session.add(restaurant17)
db.session.commit()
restaurant18 = Restaurant(RestaurantName='Noura Brasseries Ltd', Address_Line_1='16 Hobart Place', City='London', Postcode='SW1W 0HH', Telephone='020 7235 9444', Opening_Hours='Monday - Sunday: 11am - 10pm', Cuisine='Lebanese', Price='£26 - £40', Image='noura_logo.png')
db.session.add(restaurant18)
db.session.commit()
restaurant19 = Restaurant(RestaurantName='Mestizo Mexican Restaurant', Address_Line_1='103 Hampstead Road', City='London', Postcode='NW1 3EL', Telephone='020 7387 4064', Opening_Hours='Monday - Sunday: 12pm - 11pm', Cuisine='Mexican', Price='£26 & under', Image='mestizo_logo.png')
db.session.add(restaurant19)
db.session.commit()
