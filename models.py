from sqlalchemy.sql import func
from config import db

class Venue(db.Model):
    venue_id=db.Column(db.Integer,primary_key=True)
    admin_id= db.Column(db.Integer, nullable=False)
    artist_id= db.Column(db.Integer, nullable=False)
    venue_name= db.Column(db.String(100), nullable=False)
    venue_capacity= db.Column(db.Integer, nullable=False)
    venue_state=db.Column(db.String(20),nullable=False)
    venue_location = db.Column(db.String(300), nullable=False)
    venue_photo= db.Column(db.String(500), nullable=False)


class Shows (db.Model):
  show_id=db.Column(db.Integer, primary_key=True)
  show_name=db.Column(db.String(100),nullable=False)
  show_date=db.Column(db.DateTime,nullable=False)
  venue_id =db.Column(db.Integer,nullable=False)
  fan_id = db.Column(db.Integer,nullable=False)
  artist_id= db.Column(db.Integer, nullable=False)

  def __repr__(self):
          return f'<Show {self.show_name} {self.show_date}>'

  