from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()



class Fan(db.Model):
    __tablename__ = 'fan'

    fan_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(150), nullable=False)
    photo = db.Column(db.String(500))
    password = db.Column(db.String, nullable=False)
    payments = db.relationship('Payment', backref='fan', lazy=True)
    tickets = db.relationship('Ticket', backref='fan', lazy=True)

class Artist(db.Model):
    __tablename__ = 'artist'

    artist_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(500))
    username = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=False)
    photo = db.Column(db.String(500))
    seeking_venue = db.Column(db.String, nullable=False, default='OFF')
    facebook_link = db.Column(db.String(200))
    instagram_link = db.Column(db.String(100))
    seeking_description = db.Column(db.String(200), nullable=False)
    payments = db.relationship('Payment', backref='artist', lazy=True)
    venues = db.relationship('Venue', backref='artist', lazy=True)
    shows = db.relationship('Show', backref='artist', lazy=True)

class SysAdmin(db.Model):
    __tablename__ = 'sysadmin'

    admin_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=False)

class Payment(db.Model):
    __tablename__ = 'payment'

    payment_id = db.Column(db.Integer, primary_key=True)
    fan_id = db.Column(db.Integer, db.ForeignKey('fan.fan_id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('sysadmin.admin_id'), nullable=False)
    payment_method = db.Column(db.Enum('MOMO', 'OM', 'Card', name='paymentmethod'), nullable=False)
    payment_date = db.Column(db.TIMESTAMP)
    amount = db.Column(db.Numeric)

class Venue(db.Model):
    __tablename__ = 'venue'

    venue_id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    venue_name = db.Column(db.String(200), nullable=False)
    venue_capacity = db.Column(db.Integer, nullable=False)
    venue_state = db.Column(db.String(100), nullable=False, default='Available')
    venue_location = db.Column(db.String(300), nullable=False)
    venue_photo = db.Column(db.String(500), nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=True)

class Show(db.Model):
    __tablename__ = 'shows'

    show_id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(100), nullable=False)
    show_date = db.Column(db.TIMESTAMP, nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.venue_id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    tickets = db.relationship('Ticket', backref='show', lazy=True)

class Ticket(db.Model):
    __tablename__ = 'ticket'

    ticket_id = db.Column(db.Integer, primary_key=True)
    ticket_type = db.Column(db.Enum('VIP', 'PLATINUM', 'REGULAR', name='tickettype'), nullable=False)
    ticket_description = db.Column(db.String(500), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.show_id'), nullable=False)
    fan_id = db.Column(db.Integer, db.ForeignKey('fan.fan_id'), nullable=False)
    ticket_price = db.Column(db.Numeric, nullable=False, default=0)