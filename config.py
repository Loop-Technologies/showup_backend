from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)




SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(file))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Connect to the database
# TODO IMPLEMENT DATABASE URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:teming334@localhost:5432/showup'
app

db = SQLAlchemy(app)