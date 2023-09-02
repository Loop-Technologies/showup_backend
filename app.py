


from flask import render_template, redirect, request, url_for, flash, session,jsonify
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
from models import db, Fan, Artist, SysAdmin, Show,Payment, Venue
from flask_paginate import Pagination, get_page_args
import requests
from helper import calculate_amount
from datetime import datetime, time
from forms import AdminLoginForm,  FanProfileForm, ArtistProfileForm


from config import app,Mail, Message, PAYSTACK_SECRET_KEY

#  ------ IMPORTING ALL DEPENDENCIES ------APP FILE --------------------------------

login_manager = LoginManager()
# login_manager.login_view = 'app.login'
login_manager.init_app(app)



@login_manager.user_loader
def load_user(user):
    return Fan.query.get(user)

db.init_app(app)
mail = Mail(app)
engine = create_engine('postgresql://postgres:clovertt@localhost/showup')
session = sessionmaker(bind=engine)



@app.route('/')
def home():
    return render_template("./pages/landing.html")



#Fan regisration
@app.route("/fan/signup", methods = ["POST","GET"])
def fan_signup():
    if request.method == "POST":
        fullname = request.form.get('fullname')
        phonenumber = request.form.get('phonenumber')
        user_email = request.form.get('email')
        password =  request.form.get('password')
        password1 = request.form.get('password1') #password confirmation
        
        
        if password == password1:  
            
                    
            #creating a password hash
            hashed_password = generate_password_hash(password)
    
            #create a new user and save his/her data to the database
            new_fan = Fan.query.filter_by(email=user_email).first()
            
            #checking to see if the email entered has already been used
            if new_fan is not None:
                flash('That email has been used! Try another email','error')
                return render_template("./forms/fan_signup.html",fullname = fullname, phonenumber = phonenumber, user_email = user_email, password = password)
            else:
                try:
                    new_user = Fan(full_name=fullname,email=user_email, phone_number=phonenumber,password=hashed_password)
                    db.session.add(new_user)
                    db.session.commit()
                    
                    return redirect(url_for('fan_login'))
                    
                except:
                    flash('failed to register!', 'error')
                    return render_template('./forms/fan_signup.html')
             
    return render_template("./forms/fan_signup.html")
            



            
            
            
@app.route("/fan/login", methods=["GET", "POST"])
def fan_login():
    if request.method == "POST":
       
        user_email = request.form.get('email')
        password = request.form.get('password')
        
        user = Fan.query.filter_by(email=user_email).first()
        if user:
            user_password = user.password
            is_valid = check_password_hash(user_password, password)
            if is_valid:
                # login_user(user)
                # return render_template('./pages/home.html')
                 return render_template("./pages/home_venue.html")
                
            else:
                flash('Incorrect password','error')
                return render_template("./forms/login.html", user_email = user_email )
        else:
            
            flash('Account doesnt exit','error')
            # return render_template('./forms/login.html')
            redirect(url_for('fan_login'))
    return render_template("./forms/login.html")
            

  






#Artist regisration
@app.route("/artist/signup", methods = ["POST","GET"])
def artist_signup():
    if request.method == "POST":
        u_name = request.form.get('username')
        phonenumber = request.form.get('phonenumber')
        user_email = request.form.get('email')
        password =  request.form.get('password')
        password1 = request.form.get('password1') #password confirmation
    
        
        
        hashed_password = generate_password_hash(password)
       
        #create a new user and save his/her data to the database
        new_artist = Artist.query.filter_by(username=u_name).first()
        artist_email = Artist.query.filter_by(email = user_email).first()
        #checking to see if the email entered has already been used
        if new_artist is not None:
            flash('That username has been used! Try another usernanme','error')
            return render_template("./forms/artist_signup.html", username = u_name, phonenumber= phonenumber, email = user_email, password = password, password1 = password1 )

        elif artist_email is not None: 
            flash('That email has been used! Try another email','error')
            return render_template("./forms/artist_signup.html", username = u_name, phonenumber= phonenumber, email = user_email, password = password, password1 = password1 )   

        else:
            # try:
                new_user = Artist(username=u_name,email=user_email, phone_number=phonenumber,password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                #login_user(new_user, remember=True)
                    
                # return redirect(url_for('artist_login'))
                flash('Account created')
                    
            # except:
                
            #     # return render_template('./forms/artist_signup.html')
            #     flash('Account not created')
            #     return render_template("./forms/artist_signup.html", username = u_name, phonenumber= phonenumber, email = user_email, password = password, password1 = password1 )   
                
        
    return render_template("./forms/artist_signup.html")
            



            
@app.route("/showup/artist/login", methods=["GET", "POST"])
def artist_login():
    if request.method == "POST":
       
        user_email = request.form.get('email')
        password = request.form.get('password')
        
        user = Artist.query.filter_by(email = user_email).first()
        if user:
            user_password = user.password
            is_valid = check_password_hash(user_password, password)
            if is_valid:
                # return render_template('./pages/home_venue.html')
                return redirect(url_for('venues'))

            else:
                flash('Incorrect password')
                return render_template('./forms/login.html', email = user_email, password = password)
                # return redirect(url_for('venues'))
                
        else:
            
            flash('Account doesnt exist','error')
            return render_template('./forms/login.html', email = user_email, password = password)
    return render_template("./forms/login.html")
            

# -----SEARCH QUERY --------------------------------NEW ROUTES FOR FAN ARTIST AND SHOWS --------------------------------
# @app.route('/showup/navigation')
# def navigation():
#     return render_template('/pages/index.html')

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
    return render_template('/pages/results.html', 
                           Artist_result=Artist_result, 
                           Show_result=Show_result, 
                           Venue_result=Venue_result)

# @app.route('/search', methods=['POST'])
# def search():
#     if request.method == 'POST':
#         # running a search query for shows, venues, and artists
#         search_query = request.form['search_query']
#         artist_result = Artist.query.filter(Artist.username.ilike(f'%{search_query}%')).order_by(Artist.username.asc()).all()
#         show_result = Show.query.filter(Show.show_name.ilike(f'%{search_query}%')).order_by(Show.show_name.asc()).all()
#         venue_result = Venue.query.filter(Venue.venue_name.ilike(f'%{search_query}%')).order_by(Venue.venue_name()).all()

#         # if no search found from the user input, return the error page
#         if not artist_result and not show_result and not venue_result:
#             return render_template('/pages/error.html')

#         return render_template('/pages/results.html', artist_result=artist_result, show_result=show_result, venue_result=venue_result)

# @app.route('/artist/<artist_name>', methods=['GET'])
# def artist_details(artist_name):
#     artist = Artist.query.filter_by(username=artist_name).first()
#     return render_template('/pages/artist_details.html', artist=artist)

# @app.route('/venue/<venue_name>', methods=['GET'])
# def venue_details(venue_name):
#     venue = Venue.query.filter_by(venue_name=venue_name).first()
#     return render_template('/pages/venue_details.html', venue=venue)

# @app.route('/show/<show_name>', methods=['GET'])
# def show_details(show_name):
#     show = Show.query.filter_by(show_name=show_name).first()
#     return render_template('/pages/show_details.html', show=show)


# ---   CONTACTS --------------------------------US MAIL SENDING AND RECIEVER -------------------------------- REQUSET
def Submit(result):
    msg = Message("Our showup contact",
                  sender="clovistumasang82@gmail.com",
                  recipients=["tycrizclo@gmail.com", "clovistycriz@gmail.com"])

    msg.body = """
    Hello there,

    You just received a contact form.

    Name: {}
    Email: {}
    Message: {}


    regards,
    Showup AVT

    """.format(result.get('name', ''), result['email'], result['message'])

    # mail.send(msg)

# @app.route('/')
# def index():
#     return "<a href='/contact'>contact_us</a>"
@app.route("/showup/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        result = {}
        result['name'] = request.form['name']
        result['email'] = request.form['email'].replace(' ', '').lower()
        result['message'] = request.form['message']
        result['expdate'] = request.form['expdate']
        result ['cardnumber'] = request.form['cardnumber']
        Submit(result)
        print(result)

    return render_template('./forms/contact_us.html')
# return redirect(url_for('contact'))
         
# ---PAYMENT  SECTION ----------
# @app.route('/index',)
# def index():
#     return render_template('/pages/payment.html')

@app.route('/pay', methods=['GET', 'POST'])
def pay():
    try:
        print(request.form)
        # Retrieve payment details from the form
        email = request.form['email']
        ticket_id = request.form['ticket_id']

        amount = calculate_amount(ticket_id)

        paystack_url = 'https://api.paystack.co/transaction/initialize'
        headers = {
            'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
            'Content-Type': 'application/json'
        }

        data = {
            'amount': amount * 100,
            'email': email,
            'currency': '',
            'cardnumber': '282837373663322',
            'expdate': '2024',
            'mobile_money': {
                'phone': '0551234987',
                'provider': 'mtn'
            },
            'callback_url': 'http://your-callback-url.com/paystack/callback'
        }

        # Make a POST request to initialize the payment
        response = requests.post(paystack_url, headers=headers, json=data)
        payment_data = response.json()
        print(payment_data, 'payment data')

        # Check if the response contains the 'data' key
        if 'data' in payment_data:
            authorization_url = payment_data['data']['authorization_url']

            payment = Payment(amount=amount)
            db.session.add(payment)
            db.session.commit()

            return jsonify({'authorization_url': authorization_url})
        else:
            return jsonify({'error': 'Payment initialization failed'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/paystack/callback', methods=['POST'])
def payment_callback():
    try:
        payment_data = request.get_json()
        status = payment_data['status']
        reference = payment_data['reference']

        payment = Payment.query.filter_by(reference=reference).first()

        if payment:
            payment.successful = (status == 'success')
            payment.timestamp = datetime.now()
            db.session.commit()
            print(payment)
       

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)})
   
@app.route('/venue/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':


        
        return ('availability.html')


#    ---SEND EMAIL NOTIFICATION TO  ATISRT FOR ANY LATEST VENEU UPDATE  --------------------------------
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    artist = Artist.query.filter_by(email=email).first()
    # fan = Fan.query.filter_by(email=email).first()

    if artist is None:
        return "error no artist found please try again"
    send_confirmation_email(artist)
    return redirect('/home_venue')    

    # new_artist = Artist(username='', email=email)
    # # new_fan = Fan(name='', email=email)
    # db.session.add(new_artist)
    # db.session.commit()

    # send_confirmation_email(artist)
    # # send_confirmation_email(new_fan)
    # return redirect('home_venue')

def send_confirmation_email(artist):
    msg = Message('Email Notification Confirmation', sender='tycrizclo@gmail.com', recipients=[artist.email])
    msg.body = f"Thank you, {artist.username}, for subscribing to venue update notifications."
    mail.send(msg)

def send_venue_update_notification():
    # This function will be triggered whenever there are new venues in the system
    # Fetch the list of subscribed artists from the database
    subscribed_artists = Artist.query.all()
 
    for artist in subscribed_artists:
        msg = Message('New Venue Update', sender='your_email@example.com', recipients=[artist.email])
        msg.body = "There are new venues available. Check them out!"
        mail.send(msg)

# VENUE UPDATE ======= VENUE DETAILING====--------
@app.route('/showup/venues-details/<int:venue_id>', methods=['GET', 'POST'])
def venue_details(venue_id):
    venue = Venue.query.filter_by(id=venue_id).first()
    return render_template('/pages/venue_details.html', venue=venue)

@app.route('/showup/venues', methods=['GET', 'POST'])
def venues():
    all_venues = Venue.query.all()
    return render_template('/pages/home_venue.html', all_venues=all_venues)

# PROFLE MANAGEMNT SECTION FOR FAN , ARTIST AND ADMIN -------------------------------------------------#

@app.route('/fan_profile', methods=['GET', 'POST'])
def fan_profile():
    fan_obj = Fan.query.first()
    form = FanProfileForm(obj=fan_obj)

    if form.validate_on_submit():
        fan_obj.full_name = form.full_name.data
        fan_obj.phone_number = form.phone_number.data
        fan_obj.email = form.email.data

        if form.password.data:
            fan_obj.password = form.password.data

        db.session.commit()
        # Redirect to the home page after form submission
        return redirect(url_for('fan_profile'))

    hide_password = request.args.get('hide_password', False)
    return render_template('./pages/fan_profile.html', fan=fan_obj, form=form, hide_password=hide_password)


@app.route('/artist_profile', methods=['GET', 'POST'])
def artist_profile():
    artist_obj = Artist.query.first()
    form = ArtistProfileForm(obj=artist_obj)

    if form.validate_on_submit():
        artist_obj.full_name = form.full_name.data
        artist_obj.username = form.username.data
        artist_obj.phone_number = form.phone_number.data
        artist_obj.seeking_description = form.seeking_description.data
        artist_obj.seeking_venue = form.seeking_venue.data
        artist_obj.facebook_link = form.facebook_link.data
        artist_obj.instagram_link = form.instagram_link.data
        artist_obj.email = form.email.data

        if form.password.data:
            artist_obj.password = form.password.data

        db.session.commit()
        # Redirect to the home page after form submission
        return redirect(url_for('artist_profile'))

    hide_password = request.args.get('hide_password', False)
    return render_template('./pages/artist_profile.html', artist=artist_obj, form=form, hide_password=hide_password)



@app.route('/admin_profile', methods=['GET', 'POST'])
def admin_profile():
    admin_obj = Admin.query.first()
    form = AdminLoginForm(obj=admin_obj)
    if form.validate_on_submit():
        admin_obj.first_name = form.first_name.data
        admin_obj.last_name = form.last_name.data
        admin_obj.email = form.email.data
        admin_obj.password = form.password.data
        db.session.commit()
        return redirect(url_for('admin_profile'))
    hide_password = request.args.get('hide_password', False)
    return render_template('./pages/admin_profile.html', sysadmin=admin_obj, form=form, hide_password=hide_password)


@app.route('/delete_account', methods=['POST'])
def delete_account():
    profile_type = request.form.get('profile_type')
    if profile_type == 'admin':
        admin_objt = Admin.query.first()
        db.session.delete(admin_objt)
        db.session.commit()
        return redirect(url_for('home_venue'))
    elif profile_type == 'fan':
        fan_objt = Fan.query.first()
        db.session.delete(fan_objt)
        db.session.commit()
        return redirect(url_for('home_venue'))
    
    elif profile_type == 'fan':
        artist_objt = Artist.query.first()
        db.session.delete(artist_objt)
        db.session.commit()
        return redirect(url_for('home_venue'))
    
def toggle_seeking():
     if request.method == 'POST':
        toggle = request.form.get('toggle')  # Get the value of the toggle button
        if toggle == 'on':
            # Perform filtering and display results
            venue_size = request.form.get('venue_size')
            venue_location = request.form.get('venue_location')
            venue_capacity = request.form.get('venue_capacity')
            
            # Perform filtering based on the selected criteria
            # Query the show table for shows matching the criteria
            # Generate the result and display it
            result = filter_shows(venue_size, venue_location, venue_capacity)
            return render_template('result.html', result=result)
        else:
            # Toggle is off, display default page without seeking privileges
            return render_template('/pages/home_venue.html')
     else:
        # Display default page without seeking privileges
        return render_template('/pages/home_venue.html')
def filter_shows(venue_size, venue_location, venue_capacity):
    # Query the show table and filter based on selected criteria
    # Return the filtered shows
    # Example implementation:
    filtered_shows = []
    # Perform the necessary filtering logic on the show table
    # Populate the filtered_shows list with the matching shows
    return filtered_shows






# TIME AVAILABILTY FOR VENUES -------------------------=============

 
@app.route('/venue/book-time', methods=['POST', 'GET'])
def book_time():
    # Fetch venue names and IDs from the database
    venues = Venue.query.all()

    return render_template('./pages/availability.html', venues=venues)

# Route for handling form submission
booked_venues = {}

@app.route('/book', methods=['POST'])
def book_venue():
    if request.method == 'POST':
        venue_name = request.form.get('venue_name')
        venue_id = request.form.get('venue_id')
        session_name = request.form.getlist('session_name')
        time_range = request.form.get('time_range')

        if is_venue_available(venue_id, session_name, time_range):
            booking = {
                'venue_id': venue_id,
                'session_name': session_name,
                'time_range': time_range
            }
            if venue_id in booked_venues:
                booked_venues[venue_id].append(booking)
            else:
                booked_venues[venue_id] = [booking]

            success_message = f"The venue has been booked successfully."
            return jsonify({'status': 'success', 'message': success_message})
        else:
            error_message = f"Sorry, the venue is not available for the selected session(s)."
            return jsonify({'status': 'occupied', 'message': error_message})

# Function to check if a venue is available for booking in the specified time session
def is_venue_available(venue_id, session_name, time_range):
    if venue_id in booked_venues:
        bookings = booked_venues[venue_id]
        for booking in bookings:
            if booking['time_range'] == time_range:
                return False

    return True













# Route for password reset
@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']

        fan = Fan.query.filter_by(email=email).first()

        if fan:
            # Perform password reset logic
            flash('An email with password reset instructions has been sent to your email address.')
            return redirect(url_for('login'))
        else:
            flash('Invalid email. Please try again.')

    return render_template('/forms/reset_password.html')

# Route for forgot password
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

        fan = Fan.query.filter_by(email=email).first()

        if fan:
            # Perform forgot password logic
            flash('An email with instructions on how to reset your password has been sent to your email address.')
            return redirect(url_for('login'))
        else:
            flash('Invalid email. Please try again.')

    return render_template('/forms/forgot_password.html')







# @app.route('/pay', methods=['GET', 'POST'])
# def pay():
#     try:
#         print(request.form)
#         # Retrieve payment details from the form
#         email = request.form['email']
#         ticket_id = request.form['ticket_id']

#         amount = calculate_amount(ticket_id)

#         paystack_url = 'https://api.paystack.co/transaction/initialize'
#         headers = {
#             'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
#             'Content-Type': 'application/json'
#         }

#         data = {
#             'amount': amount * 100,
#             'email': email,
#             'currency': '',
#             'mobile_money': {
#                 'phone': '0551234987',
#                 'provider': 'mtn'
#             },
#             'callback_url': 'http://your-callback-url.com/paystack/callback'
#         }

#         # Make a POST request to initialize the payment
#         response = requests.post(paystack_url, headers=headers, json=data)
#         payment_data = response.json()
#         print(payment_data, 'payment data')

#         # Check if the response contains the 'data' key
#         if 'data' in payment_data:
#             authorization_url = payment_data['data']['authorization_url']

#             payment = Payment(amount=amount)
#             db.session.add(payment)
#             db.session.commit()

#             return jsonify({'authorization_url': authorization_url})
#         else:
#             return jsonify({'error': 'Payment initialization failed'})
#     except Exception as e:
#         return jsonify({'error': str(e)})


# @app.route('/paystack/callback', methods=['POST'])
# def payment_callback():
#     try:
#         payment_data = request.get_json()
#         status = payment_data['status']
#         reference = payment_data['reference']

#         payment = Payment.query.filter_by(reference=reference).first()

#         if payment:
#             payment.successful = (status == 'success')
#             payment.timestamp = datetime.now()
#             db.session.commit()
#             print(payment)

#         return jsonify({'status': 'success'})
#     except Exception as e:
#         return jsonify({'error': str(e)})




if __name__ == '__main__':
    app.run(debug=True)






