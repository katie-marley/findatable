# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

from application import db
from application.models import User

# create our database schema
# db.create_all()

db.drop_all()
db.create_all()

testPerson1 = User(FirstName='Julie', LastName='Dooley', PrefName = 'Jules', Password = 'password', Phone = '07763842259', AddressLine1='1', AddressLine2= 'The Hayes', City='Epsom', Postcode='KT186HB', Allergens='None')

db.session.add(testPerson1)

db.session.commit()
