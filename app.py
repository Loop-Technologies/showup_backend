from flask import Flask, render_template, redirect, request, url_for, flash,  Blueprint
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from models import db, fan
from config import  SECRET_KEY, SQLALCHEMY_DATABASE_URI
from count import y
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField
#from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY


db.init_app(app)

engine = create_engine('postgresql://postgres:teming334@localhost/showup')
session = sessionmaker(bind=engine)






@app.route('/')
def home():
    return render_template("./pages/home.html")



#Fan regisration
@app.route("/signup", methods = ["POST","GET"])
def signup():
    if request.method == "POST":
        fullName = request.form.get('fullname')
        phoneNumber = request.form.get('phonenumber')
        user_email = request.form.get('email')
        password =  request.form.get('password')
        password1 = request.form.get('password1') #password confirmation
        
        #creating a password hash
        hashed_password = generate_password_hash(password)
        
        

        if password == password1:
            #create a new user and save his/her data to the database
            user_user = fan.query.filter_by(email=user_email).first()
            
            #checking to see if the email entered has already been used
            if user_user is not None:
                flash('That email has been used! Try another email','error')
               
            else:
                try:
                    new_user = fan(full_name=fullName,email=user_email, phone_number=phoneNumber,password=hashed_password)
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Registered successfully', 'success')
                    
                except:
                    flash('failed to register!', 'error')
                    return render_template('./forms/RegistrationF.html')
             
        else:
            flash('Passwords do not match','error')
    return render_template("./forms/RegistrationF.html")
            
            
            
            
            
            
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
       
        user_email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password)
        
        user = fan.query.filter_by(email=user_email).first()
        #getting the user id to create a session for the user logging in
        user_id = user.fan_id
        
        user_password = user.password
        is_valid = check_password_hash(user_password, password)
        if user and is_valid:
               id = fan.query.filter_by(email = user_email).first()
               user_id = id.fan_id
              # session(user_id)
               return redirect(url_for('home'))
        else:
            flash('Invalid email or password','error')
    return render_template("./forms/login.html")
            


#tesing database connection         
@app.route('/get_data')
def get_data():
    data = fan.query.all()
    
    return render_template('./forms/test.html', data=data)



if __name__ == '__main__':  
  app.run(debug=True)