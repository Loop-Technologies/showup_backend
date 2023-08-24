import os
from flask import Flask , render_template, request,url_for, redirect

from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import func
from sqlalchemy.sql import text

from models import Shows
from config import db,app

from config import SQLALCHEMY_DATABASE_URI,SECRET_KEY

# basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)

@app.route('/')
def index():
    return render_template('pages/index.html')

# #page assign  the parameter  page_Num 
# @app.route('/display/<int:page_num>')
# def display(page_num):
#     displays = Shows.query.paginate(per_page=8,page=page_num , error_out=True)
#     return render_template('pages/display.html' , displays=displays)

#filter search results
@app.route('/show/')
def show():
    page = request.args.get('page',1,type=int)
    per_page = 4
    items = Shows.query.paginate(page=page, per_page=per_page)
    return render_template('pages/shows.html', items=items)


    # mainshow = Shows.query.all()
    # return render_template('pages/shows.html' , Shows=mainshow)
# #artist creates a show
# @app.route('/create_show/', methods=('GET','POST'))
# def create():
#     return render_template('create.html')

# def populate_db():
#     with app.open_resource('./shows.sql') as f:
#         db.session.execute(text(f.read().decode('utf-8')))
#         db.session.commit()

 
if __name__ == '__main__':   
#    with app.app_context():
#        db.create_all()
#        populate_db()
   app.run(debug=True)