import os
from flask import Flask , render_template, request,url_for, redirect

from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import func
from sqlalchemy.sql import text

from models import Shows, Venue
from config import db,app
from sqlalchemy import or_
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
    search_term = request.args.get('search_term', '')
    page = request.args.get('page',1,type=int)
    per_page = 8
    query = Shows.query

    if search_term:
        if not search_term.isnumeric():
             query = query.filter(Shows.show_name.ilike(f"%{search_term}%"))
        if search_term.isnumeric():
             query = query.filter(Shows.venue_id == search_term)

        # query = query.filter(or_(Shows.show_id.ilike(f'%{search_term}%'), Shows.show_name.ilike(f'%{search_term}%')))
        # query = query.filter(
        #     (Shows.show_id == search_term) | (Shows.show_name.ilike(f"%{search_term}%"))
        # )
    shows_pagination = query.paginate(page=page, per_page=per_page)
    shows = shows_pagination.items

    venue_ids = [show.venue_id for show in shows]
    venues = Venue.query.filter(Venue.venue_id.in_(venue_ids))
    # print([venue.venue_capacity for venue in venues])
    # venues = Venue.query.filter(Venue.venue_id.in_([show.venue_id for show in shows])).all()

    return render_template('pages/shows.html', items=shows_pagination, venues=venues)

@app.route('/venue/')
def venue():
    search= request.args.get('search_term', '')
    page = request.args.get('page',1,type=int)
    per_page = 8
    query = Venue.query
    # query = query.filter((Venue.venue_capacity == search_term) | (Venue.venue_location.ilike(f"%{search_term}%")))

    if search:
        if search.isnumeric():
             query = query.filter(Venue.venue_location.ilike(f"%{search}%"))
        if not search.isnumeric():
             query = query.filter(Venue.venue_capacity == search)
    venue_pagination = query.paginate(page=page, per_page=per_page)
    venue= venue_pagination.items
    return render_template('pages/venue.html',items=venue_pagination,venue=venue)

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