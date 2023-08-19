from flask import Flask, render_template, redirect, request, url_for, flash, Blueprint, session, make_response
from sqlalchemy import create_engine
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user
from models import db, Fan, Artist
from config import  app

#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField
#from wtforms.validators import DataRequired


Session(app)

db.init_app(app)
#login = LoginManager(app)

engine = create_engine('postgresql://postgres:teming334@localhost/showup')
session = sessionmaker(bind=engine)






@app.route('/')
def home():
    # if not session("user_email"):
        # return redirect("/pages/login.html")
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
            #eliminating spaces in password string             
            password_str = ""
            for char in password:
                if char != "":
                    password_str += char
            print(password_str)
                    
            #creating a password hash
            hashed_password = generate_password_hash(password_str)
    
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
                    #login_user(new_user, remember=True)
                    flash('Account created!', 'success')
                    return redirect(url_for('fan_login'))
                    
                except:
                    flash('failed to register!', 'error')
                    return render_template('./forms/fan_registration.html')
             
        else:
            flash('Passwords do not match','error')
    return render_template("./forms/fan_registration.html")
            


#@login.user_loader()            
            
            
            
            
@app.route("/fan/login", methods=["GET", "POST"])
def fan_login():
    if request.method == "POST":
        session["user_email"] = request.form.get('email')
        user_email = request.form.get('email')
        password = request.form.get('password')
         
        user = Fan.query.filter_by(email=user_email).first()
        user_password = user.password
        is_valid = check_password_hash(user_password, password)
        if is_valid and user:
            return render_template('./pages/home.html', user=user)
        else:
            
            flash('Invalid email or password','error')
            return render_template('./forms/fan_login.html',email = user_email)
    return render_template("./forms/fan_login.html")
            
@app.route("/fan/logout")
def logout():
    session["fullname"] = None
    return redirect("/pages/login.html")
  
  
admin = Admin(app)  
admin.add_view(ModelView(Fan, db.session))
admin.add_view(ModelView(Artist, db.session))
  




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
            password_str = ""
            for char in password:
                if char != "":
                    password_str += char
            #creating a password hash
            hashed_password = generate_password_hash(password_str)
       
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
                    return redirect(url_for('artist_login'))
                    
                except:
                    flash('failed to register!', 'error')
                    return render_template('./forms/artist_registration.html')
             
        else:
            flash('Passwords do not match','error')
    return render_template("./forms/artist_registration.html")
            



            
@app.route("/artist/login", methods=["GET", "POST"])
def artist_login():
    if request.method == "POST":
       
        user_name = request.form.get('username')
        password = request.form.get('password')
        
        user = Artist.query.filter_by(username = user_name).first()
        user_password = user.password
        is_valid = check_password_hash(user_password, password)
        if is_valid and user:
            return render_template('./pages/home.html', user=user)
        else:
            
            flash('Invalid email or password','error')
            return render_template('./forms/login.html',username = user_name)
    return render_template("./forms/artist_login.html")


    


#...
       




if __name__ == '__main__':  
  app.run(debug=True)