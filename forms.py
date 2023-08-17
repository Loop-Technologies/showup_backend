from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, Length

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



class ArtistProfileForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    seeking_venue = StringField('Seeking Venue')
    facebook_link = StringField('Facebook Link')
    instagram_link = StringField('Instagram Link')
    seeking_description = StringField('Seeking Description', validators=[DataRequired(), Length(max=200)])
    photo = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])