from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
# basedir = os.path.abspath(os.path.dirname(file))

default_filepath = os.getcwd()
print(default_filepath)

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Zonecoco2003.@localhost:5432/postgres'
db = SQLAlchemy(app)
# Connect to the database
# TODO IMPLEMENT DATABASE URL
