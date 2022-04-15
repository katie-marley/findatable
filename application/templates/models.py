from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# want to store the username and password #


class User(db.Model):
    """User Model"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
