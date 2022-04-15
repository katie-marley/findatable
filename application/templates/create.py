from application import db
from application.models import User

# create our database schema
# db.create_all()

db.drop_all()
db.create_all()

testPerson1 = User(username='Julie', password='Dooley')

db.session.add(testPerson1)

db.session.commit()
