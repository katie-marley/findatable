from flask_sqlalchemy import SQLAlchemy
from application import db

# want to store the username and password #


class Users(db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
