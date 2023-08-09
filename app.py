from flask import Flask, render_template, redirect, request, url_for, flash,  Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import sessionmaker
import  models
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField
#from wtforms.validators import DataRequired

app = Flask(__name__)

from models import db, app



engine = create_engine('postgresql://postgres:teming334@localhost/showup')

session = sessionmaker(bind=engine)
session = session()


@app.route('/home')
def home():
    return render_template("./pages/home.html")



#Fan regisration
@app.route("/signup", methods = ["POST","GET"])
def signup():
    if request.method == "POST":
        fullName = request.form.get('fullmname')
        phoneNumber = request.form.get('phonnumber')
        user_email = request.form.get('email')
        password =  request.form.get('password')
        password1 = request.form.get('password1') #password confirmation
        
       
        if password == password1:
            #create a new user and save his/her data to the database
            user_password = generate_password_hash(password)
            try:
                new_user = models.fan(admin_id =1, full_name=fullName, phone_number=phoneNumber, email=user_email,password=user_password)
                db.session.add(new_user)
                db.session.commit()
                flash('success', 'success')
            except:
                flash('failed!', 'error')
        else:
            flash('Passwords do not match', category='error')
    return render_template("./forms/RegistrationF.html")
            
            
            
            
            
            
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_email = request.form.get('email')
        password = request.form.get('password')
        user = models.fan.query.filter_by(email=user_email).first()
        if user and user.check_password(password):
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', category='error')
    return render_template("./forms/login.html")
            
            
@app.route('/get_data')
def get_data():
    data = models.fan.query.filter_by(admin_id = 4).all()
    data = list(data)   
    return data 



if __name__ == '__main__':  
  app.run(debug=True)