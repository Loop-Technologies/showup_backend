from flask import Flask, render_template, redirect, request, url_for, flash, Blueprint, session
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
# from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
from models import db, Fan, Artist, SysAdmin, Show, Payment, Venue, Ticket
# from flask_paginate import Pagination, get_page_args
# from config import  SECRET_KEY, SQLALCHEMY_DATABASE_URI
from config import app




engine = create_engine('postgresql://postgres:teming334@localhost/showup')
session = sessionmaker(bind=engine)


@app.route("/")
def home():
    return render_template("/pages/index.html")


@app.route("/fan_data", methods=["GET", "POST"])    
def fan_data():
    if request.method == "POST":
        search_str = request.form.get('search')
        fans = Fan.query.filter(Fan.full_name.ilike(f'%{search_str}%')).all()
        if fans:
         return render_template("/pages/fans.html", fans = fans)
    # else:   
    # venues = Fan.query.paginate(page=1 per_page = 6, error_out = False)
    fans = Fan.query.all()
    
    return render_template("/pages/fans.html", fans = fans)


@app.route("/fan/delete/<int:fan_id>", methods =["GET","POST"])
def delete_fan_account(fan_id):
    if request.method == "POST":
        account = Fan.query.get(fan_id)
        print(account)
        db.session.delete(account)
        db.session.commit()
    return redirect(url_for('fan_data'))


@app.route("/artist_data", methods = ["GET", "POST"])
def artist_data():
    if request.method == "POST":
        search_str = request.form.get('search')
       
        artists = Artist.query.filter(Artist.username.ilike(f'%{search_str}%')).all()
        if artists:
         return render_template("/pages/artist.html", artists = artists)
       
    artists = Artist.query.order_by(Artist.artist_id.asc()).all()  
    
    return  render_template("/pages/artist.html", artists = artists)


@app.route("/artists/delete/<int:artist_id>", methods =["GET","POST"])
def delete_account(artist_id):
    if request.method == "POST":
        account = Artist.query.get(artist_id)
        print(account)
        db.session.delete(account)
        db.session.commit()
    return redirect(url_for('artist_data'))

    


@app.route("/shows", methods=["GET", "POST"])
def shows():
    if request.method == "POST":
        name = request.form.get('name')
        date = request.form.get('date')
        artist = request.form.get('artist')
        venue = request.form.get('venue')
        poster = request.form.get('poster')
         
        print(poster)  
        show_owner = Artist.query.filter_by(username = artist).first()
        if show_owner:
            artist_id = show_owner.artist_id
                
            venue_for_show = Venue.query.filter_by(venue_name = venue).first()
            venue_id = venue_for_show.venue_id
            # if venue_for_show.venue_state == 'Reserved':
            #     return "that venue is not available"   
            # else:
            new_show = Show(show_name = name, show_date = date, venue_id = venue_id, artist_id = artist_id, poster = poster)
            db.session.add(new_show)
            db.session.commit()
        else:
            return "that artist does not exist"
    venues =Venue.query.all()
    shows = Show.query.order_by(Show.show_id.asc()).all()
    artists = Artist.query.all()
    return  render_template("/pages/shows.html", shows = shows, artists = artists, venues = venues)


# function for editing shows 
@app.route('/shows/edit/<int:s_id>', methods=['POST', 'GET'])
def update_shows(s_id):
    
    if request.method == "POST":
        
        updated_name = request.form.get('name')
        updated_date = request.form.get('date')
        updated_venue = request.form.get('venue')
        updated_artist = request.form.get('artist')
        updated_poster = request.form.get('poster')
      
        
        try:
            # db.session.query(Venue).filter_by(venue_id = v_id).update(venue_id = v_id, artist_id = updated_artist_id, venue_name = updated_name, venue_capacity = updated_capacity, venue_state = updated_state, venue_location = updated_location, venue_photo = updated_photo, show = updated_show)
            show_update = Show.query.filter_by(show_id = s_id).first()
            # show_update.show_id = s_id
            show_update.name = updated_name
            show_update.venue_id = updated_venue
            show_update.artist_id = updated_artist
            show_update.poster = updated_poster
            show_update.date = updated_date
           
            db.session.commit()
            # venues = Venue.query.filter_by(venue_id=v_id).all()
            # return render_template("/pages/edit_venue.html", venues = venues )
            return redirect(url_for('shows'))
        except:
            
            return "error"
    shows = Show.query.filter_by(show_id=s_id).all()
    return render_template("/pages/edit_show.html", shows = shows )



#function for deleting shows 
@app.route('/shows/delete/<int:show_id>', methods = ['POST'])
def delete_shows(show_id):
    if request.method == 'POST':
        pending_show = Show.query.get(show_id)
        db.session.delete(pending_show)
        db.session.commit()
    return redirect(url_for('shows'))




#displaying venues and implementing search for venues
@app.route("/venues", methods=["GET", "POST"])
def venues():
     if request.method == "POST":
        search_str = request.form.get('search')
        
        
        #getting data for new venue to be created 
        
        name = request.form.get('name')
        capacity = request.form.get('capacity')
        price = request.form.get('price')
        state = request.form.get('state')
        location = request.form.get('location')
        photo =  request.form.get('photo')
        
        #adding a new venue to the database
        if search_str is None:
            new_venue = Venue(venue_name = name, venue_capacity = capacity, venue_price = price, venue_state = state, venue_location = location, venue_photo = photo)
            db.session.add(new_venue)
            db.session.commit()
            
        
        
        
        else:
        #query to display items relating to user search
            venues = Venue.query.filter(Venue.venue_name.ilike(f'%{search_str}%')).all()
            if venues:
                try:
                    return render_template("/pages/venues.html", venues = venues) 
                except:
                    return render_template("/pages/no_results.html")     

    #displaying all venues available in the database 
    
     booked_venues = Venue.query.filter_by(venue_state = 'Reserved').order_by(Venue.venue_id.asc()).all()
 
     venues = Venue.query.order_by(Venue.venue_id.asc()).all()
     return  render_template("/pages/venues.html", venues = venues, booked_venues = booked_venues)
   




#function for deleting venues 
@app.route('/venues/delete/<int:venue_id>', methods = ['POST'])
def delete_venue(venue_id):
    if request.method == 'POST':
        pending_venue = Venue.query.get(venue_id)
        db.session.delete(pending_venue)
        db.session.commit()
    return redirect(url_for('venues'))



# function for editing venues 
@app.route('/venues/edit/<int:v_id>', methods=['POST', 'GET'])
def update_venue(v_id):
    
    if request.method == "POST":
        updated_artist_id = request.form.get('a_id')
        updated_name = request.form.get('name')
        updated_capacity = request.form.get('capacity')
        updated_price = request.form.get('price')
        updated_state = request.form.get('state')
        updated_location = request.form.get('location')
        updated_photo = request.form.get('photo')
        updated_show = request.form.get('show')   
        print( updated_artist_id, updated_name, updated_capacity, updated_state, updated_location, updated_photo,updated_show)     
        
        try:
            # db.session.query(Venue).filter_by(venue_id = v_id).update(venue_id = v_id, artist_id = updated_artist_id, venue_name = updated_name, venue_capacity = updated_capacity, venue_state = updated_state, venue_location = updated_location, venue_photo = updated_photo, show = updated_show)
            venue_update = Venue.query.filter_by(venue_id = v_id).first()
            venue_update.venue_id = v_id
            venue_update.artist_id = updated_artist_id
            venue_update.venue_name = updated_name
            venue_update.venue_capacity = updated_capacity
            venue_update.venue_price = updated_price
            venue_update.venue_state = updated_state
            venue_update.venue_location = updated_location
            venue_update.venue_photo = updated_photo
            db.session.commit()
            # venues = Venue.query.filter_by(venue_id=v_id).all()
            # return render_template("/pages/edit_venue.html", venues = venues )
            return redirect(url_for('venues'))
        except:
            
            return "error"
        

        
        
    venues = Venue.query.filter_by(venue_id=v_id).all()
    return render_template("/pages/edit_venue.html", venues = venues )


@app.route('/tickets', methods = ['GET', 'POST'])
def tickets():
    if request.method == 'POST':
        search_str = request.form.get('search')
        t_type = request.form.get('type')
        show = request.form.get('show')
        description = request.form.get('description')
        price = request.form.get('price')
        
        print(t_type, show, description, price)
        print(search_str)
        
        
        #ensuring that tickets can only be created for existing shows
        valid_show = Show.query.filter_by(show_name=show).first()
        if search_str is None: 
            if valid_show:
                
                try:
                    #creating a ticket after confirming that the show exists
                    new_ticket = Ticket(ticket_type=t_type,show_id = valid_show.show_id, ticket_description = description, ticket_price = price)
                    db.session.add(new_ticket)
                    db.session.commit()
                except:
                    return "Error! Ticket was not added"
            else:
                return "That show does not exist"
        else:
              #performing a search query
              tickets = Ticket.query.filter(Ticket.show_id.ilike(f'%{search_str}%')).all()
              
              if tickets:
                    return render_template("/pages/tickets.html", tickets = tickets)
              else:
                    return render_template("/pages/no_results.html")
        
        
    # displaying all tickets in the database  
    tickets = Ticket.query.all()
    shows = Show.query.all()
    # for ticket in tickets:
    #  shows = Show.query.filter_by(show_name = ticket.show_name).all()
    #  return shows
    return render_template("/pages/tickets.html", tickets = tickets, shows = shows)
    # return render_template("/pages/tickets.html", combined_data = zip(tickets, shows))
    
    
    
#edtitng tickets
@app.route('/tickets/edit/<int:ticket_id>', methods = ['POST', 'GET'])
def edit_tickets(ticket_id):
    if request.method == 'POST':
        t_type = request.form.get('type')
        description = request.form.get('description')
        show = request.form.get('show')
        price = request.form.get('price')    
        
        pending_ticket =  Ticket.query.filter_by(ticket_id=ticket_id).first()
        if pending_ticket:
            pending_ticket.ticket_type = t_type
            pending_ticket.ticket_description = description
            pending_ticket.show = show
            pending_ticket.price = price
            db.session.commit()
            return redirect(url_for('tickets'))
        else:
            return "Ticket was not updated"
    shows = Show.query.all()    
    pending_ticket =  Ticket.query.filter_by(ticket_id=ticket_id).order_by(Ticket.ticket_id.asc()).all()
    return render_template('/pages/edit_tickets.html', pending_ticket = pending_ticket, shows = shows)

#function for deleting tickets 
@app.route('/tickets/delete/<int:ticket_id>', methods = ['POST'])
def delete_tickets(ticket_id):
    if request.method == 'POST':
        pending_ticket = Ticket.query.get(ticket_id)
        db.session.delete(pending_ticket)
        db.session.commit()
    return redirect(url_for('tickets'))


@app.route('/payments', methods=['POST','GET'])
def payments():
    return  render_template('pages/payments.html')
    
if __name__ == '__main__':
   app.run(debug=True)

