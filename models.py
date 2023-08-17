# from config import  app
# from sqlalchemy.sql import func
# import hashlib
# from sqlalchemy import UniqueConstraint, CheckConstraint
# from flask_sqlalchemy import SQLAlchemy
# # Database Models



# db = SQLAlchemy()

# class Artist(db.Model):
#     artist_id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(500), nullable=False, unique=True)
#     username = db.Column(db.String(200), nullable=False, unique=True)
#     email = db.Column(db.String(150), nullable=False, unique=True)
#     phone_number = db.Column(db.String(150), nullable=False, unique=True)
#     password = db.Column(db.String(), nullable=False)
#     image = db.Column(db.String(500))
#     seeking_venue = db.Column(db.String(), nullable=False, default='OFF')
#     facebook_link = db.Column(db.String(200), unique=True)
#     instagram_link = db.Column(db.String(100), unique=True)
#     seeking_description = db.Column(db.String(200), nullable=False)



# class Fan(db.Model):
#     # __tablename__ = 'fan'
#     fan_id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(100), nullable=False)
#     phone_number = db.Column(db.String(20), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     photo = db.Column(db.String(255), nullable=True)

#     __table_args__ = (
#         UniqueConstraint('email', name='unique_email'),
#         UniqueConstraint('phone_number', name='unique_phone_number'),
#         CheckConstraint('length(full_name) > 0', name='non_empty_full_name'),
#         CheckConstraint('length(password) > 0', name='non_empty_password'),
#     )

# class Admin(db.Model):
#     __tablename__ = 'sysadmin'
#     admin_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(100), nullable=False)
#     last_name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)

#     def set_password(self, password):
#         # Hash the password before storing it
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#         self.password = hashed_password

#     def check_password(self, password):
#         # Compare the provided password with the stored hashed password
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#         return self.password == hashed_password


from config import db
from sqlalchemy.sql import func
import hashlib

# Database Models

class Artist(db.Model):
    __tablename__ = 'artist'
    artist_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    seeking_venue = db.Column(db.String(), nullable=False, default='OFF')
    facebook_link = db.Column(db.String(200), unique=True)
    instagram_link = db.Column(db.String(100), unique=True)
    seeking_description = db.Column(db.String(200), nullable=False)
    photo = db.Column(db.String(255), nullable=True)


from sqlalchemy import UniqueConstraint, CheckConstraint

class Fan(db.Model):
    __tablename__ = 'fan'
    fan_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(255), nullable=True)

    __table_args__ = (
        UniqueConstraint('email', name='unique_email'),
        UniqueConstraint('phone_number', name='unique_phone_number'),
        CheckConstraint('length(full_name) > 0', name='non_empty_full_name'),
        CheckConstraint('length(password) > 0', name='non_empty_password'),
    )

class Admin(db.Model):
    __tablename__ = 'sysadmin'
    admin_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.password = hashed_password

    def check_password(self, password):
        # Compare the provided password with the stored hashed password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return self.password == hashed_password