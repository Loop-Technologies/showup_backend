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
                 return render_template("./pages/landing.html")
                
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
                return render_template('./pages/landing.html')
            else:
                flash('Incorrect password')
                return render_template('./forms/login.html', email = user_email, password = password)
                
        else:
            
            flash('Account doesnt exist','error')
            return render_template('./forms/login.html', email = user_email, password = password)
    return render_template("./forms/login.html")
            

if __name__ == '__main__':  
  app.run(debug=True)