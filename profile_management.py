from flask import Flask, render_template, redirect, flash, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = '33'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Zonecoco2003.@localhost:5432/postgres'
# Disable CSRF protection
app.config['WTF_CSRF_ENABLED'] = False

db = SQLAlchemy(app)

# Database Models


class Fan(db.Model):
    fan_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=False)
    photo = db.Column(db.String(500))


class Admin(db.Model):
    __tablename__ = 'sysadmin'
    admin_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

# Forms


class AdminLoginForm(FlaskForm):
    first_name = StringField('Full Name', validators=[InputRequired()])
    last_name = StringField('Full Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])


class FanProfileForm(FlaskForm):
    full_name = StringField('Full Name', validators=[InputRequired()])
    phone_number = StringField('Phone Number', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])

    # Routes


@app.route('/')
def home():
    return 'Welcome to the profile management system!'


@app.route('/fan', methods=['GET', 'POST'])
def fan_profile():
    fan = Fan.query.first()
    # fan = get_fan()
    form = FanProfileForm(obj=fan)
    if form.validate_on_submit():
        fan.full_name = form.full_name.data
        fan.phone_number = form.phone_number.data
        fan.password = form.password.data
        fan.email = form.email.data
        db.session.commit()
        flash('Fan profile updated successfully!', 'success')
        return redirect(url_for('fan_profile'))
    return render_template('./forms/fan.html', fan=fan)


@app.route('/admin', methods=['GET', 'POST'])
def admin_profile():
    sysadmin = Admin.query.first()
    form = AdminLoginForm(obj=sysadmin)
    if form.validate_on_submit():
        sysadmin.first_name = form.first_name.data
        sysadmin.second_name = form.last_name.data
        sysadmin.email = form.email.data
        sysadmin.password = form.password.data
        db.session.commit()
        flash('Admin profile updated successfully!', 'success')
        return redirect(url_for('admin_profile'))
    return render_template('./forms/admin.html', sysadmin=sysadmin)


@app.route('/delete', methods=['POST'])
def delete_account():
    profile_type = request.form.get('profile_type')
    if profile_type == 'admin':
        # Delete admin profile
        sysadmin = Admin.query.first()
        db.session.delete(sysadmin)
        db.session.commit()
        flash('Admin profile deleted successfully!', 'success')
        return redirect(url_for('home'))
    elif profile_type == 'fan':
        # Delete fan profile
        fan = Fan.query.first()
        db.session.delete(fan)
        db.session.commit()
        flash('Fan profile deleted successfully!', 'success')
        return redirect(url_for('home'))
    # elif profile_type == 'artist':
    #     # Delete artist profile
    #     artist = Artist.query.first()
    #     db.session.delete(artist)
    #     db.session.commit()
    #     flash('Artist profile deleted successfully!', 'success')
    #     return redirect(url_for('home'))
    else:
        flash('Invalid profile type!', 'error')
        return redirect


if __name__ == '__main__':
    app.run(debug=True)
