# from  flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from config import db

# db = SQLAlchemy(app)


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))


    def __init__(self, amount, email, phone, country):
        self.amount = amount
        self.email = email
        self.phone = phone
  