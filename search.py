

# from flask import Flask, render_template, request, jsonify
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from models import db, fan, artist


# app = Flask(__name__)
# engine = create_engine('postgresql://postgres:clovertt@localhost/shows')
# Session = sessionmaker(bind=engine)
# Base = declarative_base()

# db.init_app(app)


# @app.route('/', methods=['GET', 'POST'])
# def search():
#     if request.method == 'POST':
#         # Get the search query from the user input
#         search_query = request.form.get('search_query')

#         # Query the database using SQLAlchemy
#         session = Session()
#         results = session.query(Item).filter(Item.name.ilike(f'%{search_query}%')).all()

#         # Process the results as needed
#         processed_results = []
#         for item in results:
#             processed_results.append({
#                 'id': item.id,
#                 'name': item.name,
                
#             })

#         # Return the processed results as a JSON response
#         return jsonify(processed_results)

#     return render_template('index.html')

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
#     app.run()


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db
from config import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:clovertt@localhost/showup'


db.init_app(app)
from models import db, Fan, Artist, Show, Venue

    # Add other artist fields as necessary


@app.route('/')
def index():
    return render_template('/pages/index.html')


# search route ... can search for any radom thing here using the search field and getthe resuls 
@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
    # running a search query  for shows veneus artis 
        search_query = request.form['search_query']
        Artist_result = Artist.query.filter(Artist.username.ilike(f'%{search_query}%')).all()
        Show_result = Show.query.filter(Show.show_name.ilike(f'%{search_query}%')).all()
        Venue_result = Venue.query.filter(Venue.venue_name.ilike(f'%{search_query}%')).all()


# if no search found from the user input, return the error page 
    if not Artist_result and not Show_result and not Venue_result:
        return render_template('/pages/error.html')
    return render_template('/pages/result.html', Artist_result=Artist_result, Show_result=Show_result, Venue_result=Venue_result)



if __name__ == '__main__':
    app.run()

