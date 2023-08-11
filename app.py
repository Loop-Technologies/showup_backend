import os
from flask import Flask , render_template, request,url_for, redirect

from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import func
from sqlalchemy.sql import text

from models import Show
from config import db

#from config import SQLALCHEMY_DATABASE_URI,SECRET_KEY

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:LANYE0200@localhost:5432/showup' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def index():
    return render_template('pages/index.html')

@app.route("/shows/")
def shows():
    mainshow = Show.query.all()
    return render_template('pages/index.html', shows=mainshow)



# def populate_db():
#     with app.open_resource('./shows.sql') as f:
#         db.session.execute(text(f.read().decode('utf-8')))
#         db.session.commit()

 
if __name__ == '__main__':
  #  with app.app_context():
      #  db.create_all()
      #  populate_db()
   app.run(debug=True)