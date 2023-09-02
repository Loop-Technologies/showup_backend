
# from flask import Flask 
# from flask import Flask, request, jsonify, render_template
# import os
# from datetime import datetime, time
# from sqlalchemy import Date, DateTime
# from flask import Flask, render_template , request , redirect, sessions, url_for
# from sqlalchemy import create_engine
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
# from sqlalchemy.orm import sessionmaker
# from config import SQLALCHEMY_DATABASE_URI
# from sqlalchemy import create_engine, column, Integer, String
# from models import Venue, db ,sessions
# basedir = os.path.abspath(os.path.dirname(__file__))


# SECRET_KEY = os.urandom(32)
# app = Flask(__name__)
# app.secret_key='hmm'
# #app.config['SESSION_TYPE'] = 'filesystem'



# app.config['SQLALCHEMY_DATABASE_URI'] =SQLALCHEMY_DATABASE_URI

# db.init_app(app)

# engine =create_engine('postgresql://postgres:12345@localhost/showup')
# session= sessionmaker(bind=engine)
# #admin view of the db
# admin = Admin(app)
# admin.add_view(ModelView(Venue, db.session))
# admin.add_view(ModelView(sessions, db.session))
# #artist_id = 123  # Variable declaration














# # Route for the booking form
# @app.route('/', methods=['POST', 'GET'])
# def booking_form():
#     # Fetch venue names and IDs from the database
#     venues = Venue.query.all()

#     return render_template('./forms/index.html', venues=venues)

# # Route for handling form submission




# booked_venues = {}

# @app.route('/book', methods=['POST'])
# def book_venue():
#     if request.method == 'POST':
#         venue_name = request.form.get('venue_name')
#         venue_id = request.form.get('venue_id')
#         session_name = request.form.getlist('session_name')
#         time_range = request.form.get('time_range')

#         if is_venue_available(venue_id, session_name, time_range):
#             booking = {
#                 'venue_id': venue_id,
#                 'session_name': session_name,
#                 'time_range': time_range
#             }
#             if venue_id in booked_venues:
#                 booked_venues[venue_id].append(booking)
#             else:
#                 booked_venues[venue_id] = [booking]

#             success_message = f"The venue has been booked successfully."
#             return jsonify({'status': 'success', 'message': success_message})
#         else:
#             error_message = f"Sorry, the venue is not available for the selected session(s)."
#             return jsonify({'status': 'occupied', 'message': error_message})

# # Function to check if a venue is available for booking in the specified time session
# def is_venue_available(venue_id, session_name, time_range):
#     if venue_id in booked_venues:
#         bookings = booked_venues[venue_id]
#         for booking in bookings:
#             if booking['time_range'] == time_range:
#                 return False

#     return True
# def get_availability():
#     if request.method == 'GET':
#         venue_id = request.args.get('venue_id')
#         session_name = request.args.get('session_name')

#         if venue_id in booked_venues:
#             bookings = booked_venues[venue_id]
#             for booking in bookings:
#                 if session_name in booking['session_name']:
#                     return jsonify({'status': 'occupied', 'message': f"The venue is booked for the session {session_name}"})

#         return jsonify({'status': 'available', 'message': f"The venue is available for the session {session_name}"})



# if __name__ == '__main__':
#     app.run()

