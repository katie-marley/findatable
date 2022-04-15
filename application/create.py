# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

from application import db
from application.models import Users

db.drop_all()
db.create_all()
testPerson1 = Users(username='Julie', password='Dooley')
db.session.add(testPerson1)
db.session.commit()
