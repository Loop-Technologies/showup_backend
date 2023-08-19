from flask import Flask, render_template, redirect, request, url_for, flash, Blueprint, session
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
from models import db, Fan, Artist, SysAdmin, Show,Payment
from flask_paginate import Pagination, get_page_args
# from config import  SECRET_KEY, SQLALCHEMY_DATABASE_URI
from config import app




# app = Flask(__name__)

# from venue_listing import venue_listing as venue_listing
# app.register_blueprint(venue_listing)


# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SECRET_KEY'] = SECRET_KEY




login_manager = LoginManager()
# login_manager.login_view = 'app.login'
login_manager.init_app(app)



@login_manager.user_loader
def load_user(user):
    return Fan.query.get(user)

db.init_app(app)

engine = create_engine('postgresql://postgres:teming334@localhost/showup')
session = sessionmaker(bind=engine)






@app.route('/')
def home():
    return render_template("./pages/home.html")



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
               
            else:
                try:
                    new_user = Fan(full_name=fullname,email=user_email, phone_number=phonenumber,password=hashed_password)
                    db.session.add(new_user)
                    db.session.commit()
                    
                    flash('Account created!', 'success')
                    return redirect(url_for('fan_login'))
                    
                except:
                    flash('failed to register!', 'error')
                    return render_template('./forms/fan_registration.html')
             
        else:
            flash('Passwords do not match','error')
    return render_template("./forms/fan_registration.html")
            



            
            
            
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
                return render_template('./pages/home.html')
            else:
                flash('Incorrect password','error')
        else:
            
            flash('Account doesnt exit','error')
            return render_template('./forms/fan_login.html',email = user_email)
    return render_template("./forms/fan_login.html")
            

  


#admin views for the various tables in the database
admin = Admin(app)  
admin.add_view(ModelView(Fan, db.session))
admin.add_view(ModelView(Artist, db.session))
admin.add_view(ModelView(SysAdmin, db.session))
  




#tesing database connection         
@app.route('/get_data')
def get_fan_data():
    data = Fan.query.all()
    
    return render_template('./forms/test.html', data=data)


#tesing database connection         
@app.route('/get_artist_data')
def get_artist_data():
    data = Artist.query.all()
    
    return render_template('./forms/test1.html', data=data)



#Artist regisration
@app.route("/artist/signup", methods = ["POST","GET"])
def artist_signup():
    if request.method == "POST":
        u_name = request.form.get('username')
        phonenumber = request.form.get('phonenumber')
        user_email = request.form.get('email')
        password =  request.form.get('password')
        password1 = request.form.get('password1') #password confirmation
    
        if password == password1:
        

            #eliminating spaces in password string             
            # password_str = ""
            # for char in password:
            #     if char != "":
            #         password_str += char
            #creating a password hash
            hashed_password = generate_password_hash(password)
       
            #create a new user and save his/her data to the database
            new_artist = Artist.query.filter_by(username=u_name).first()
            
            #checking to see if the email entered has already been used
            if new_artist is not None:
                flash('That username has been used! Try another email','error')
               
            else:
                try:
                    new_user = Artist(username=u_name,email=user_email, phone_number=phonenumber,password=hashed_password)
                    db.session.add(new_user)
                    db.session.commit()
                    #login_user(new_user, remember=True)
                    flash('Account created!', 'success')
                    # return redirect(url_for('artist_login'))
                    
                except:
                    flash('failed to register!', 'error')
                    return render_template('./forms/artist_registration.html')
             
        else:
            flash('Passwords do not match','error')
    return render_template("./forms/artist_registration.html")
            



            
@app.route("/artist/login", methods=["GET", "POST"])
def artist_login():
    if request.method == "POST":
       
        user_email = request.form.get('email')
        password = request.form.get('password')
        
        user = Artist.query.filter_by(email = user_email).first()
        if user:
            user_password = user.password
            is_valid = check_password_hash(user_password, password)
            if is_valid:
                return render_template('./pages/home.html')
            else:
                flash('Invalid password')
        else:
            
            flash('Account doesnt exist','error')
            return render_template('./forms/login.html')
    return render_template("./forms/artist_login.html")
            








# #pagination of venues 
# @app.route("/venues", methods = ["GET", "POST"])
# def venues():
 
#     venues = fan.query.paginate(page=1,per_page = 4)
#     print(venues.items)
#     print(venues.pages)
#     Paginated_items= []
#     #  for i in range (venues.pages):
        
#     return render_template("pages/venues.html",venues = venues)    
            
# #loading more items to the page
# @app.route("/venues/load_more",methods = ["GET", "POST"])
# def load_more():
#     venues = fan.query.paginate(page=2,per_page = 4)
#     if request.method == "post":
        
#         print(venues.items)           
#         # return render_template("pages/venues.html",venues = venues)


#     return render_template("pages/venues.html",venues = venues)



@app.route("/venues/<int:page_num>")
def venues_listing(page_num):
    venues = Fan.query.paginate(page=page_num, per_page = 6, error_out = False)
    return render_template("pages/venues.html",venues = venues)



if __name__ == '__main__':  
  app.run(debug=True)