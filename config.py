import os
from flask_sqlalchemy import SQLAlchemy
# import model
from flask import Flask
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)


# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Connect to the database
# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:teming334@localhost/showup'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:clovertt@localhost/showup'  # Replace with your PostgreSQL database URI
db = SQLAlchemy(app)



# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SECRET_KEY'] = SECRET_KEY