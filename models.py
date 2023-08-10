from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()





class fan(db.Model):
    __tablename__ = 'fan'
    fan_id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, nullable=False)
    full_name = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    


class artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(500), nullable=False)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    #image = db.Column(db.bytea)
    #seeking venue = db.Column(db.
    facebook_link = db.Column(db.String(200))
    instagram_link = db.Column(db.String(200))