from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileAllowed

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
photo = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])