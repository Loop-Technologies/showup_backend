from flask import Flask 
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)




SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname('showup_backend'))
# basedir = os.path.abspath(os.path.dirname(file))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Connect to the database
# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:LANYE0200@localhost:5432/showup'   

db = SQLAlchemy()