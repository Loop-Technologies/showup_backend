from flask import flask, Blueprint, render_template
from models import db, fan, artist

venues = Blueprint('venues', __name__)

#pagination of venues 
@venues.route("/venues", methods = ["GET", "POST"])
def venues():
 
        
 #venues = fan.query.limit(10).all().paginate(per_page = 3)
         
 venues = fan.query.all().paginate(per_page = 3)
 print(venues.items)
 print(venues.page)
 return render_template("pages/venues.html",venues = venues)
        
    #return render_template("pages/venues.html") 