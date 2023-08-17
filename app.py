# from flask import render_template, redirect, url_for, request
# from config import app
# from models import Admin, Fan, Artist
# from models import db
# from forms import AdminLoginForm,  FanProfileForm, ArtistProfileForm
# from flask_sqlalchemy import SQLAlchemy

# @app.route('/')
# def home():
#     return render_template('./forms/home.html')

# #  Fan's Route


# @app.route('/fan_profile/<int:fan_id>', methods=['GET'])
# def fan_profile(fan_id):
#     form = FanProfileForm(obj=fan)
#     fan = Fan.query.get(fan_id)
#     if fan:
#         return render_template('./forms/fan_profile.html', fan=fan, form=form)
#     else:
#         # Handle fan not found case
#         return render_template('fan_not_found.html')


# @app.route('/fan_edit_profile/<int:fan_id>', methods=['GET', 'POST'])
# def fan_edit_profile(fan_id):
#     fan= Fan.query.get(fan_id)
#     form = FanProfileForm(obj=fan)

#     if form.validate_on_submit():

#         form.populate_obj(fan)

#         if form.password.data:
#             fan.password = form.password.data

#         db.session.commit()
#         # Redirect to the home page after form submission
#         return redirect(url_for('fan_profile'))

#     hide_password = request.args.get('hide_password', False)
#     return render_template('./forms/fan_profile.html', fan=fan, form=form, hide_password=hide_password)


# @app.route('/fan_delete_profile/<int:fan_id>', methods=['POST'])
# def delete_fan(fan_id):
#     fan_obj = Fan.query.get(fan_id)
#     # if not fan_obj:
#     #     # Handle artist not found case
#     #     return render_template('admin_not_found.html')

#     db.session.delete(fan_obj)
#     db.session.commit()
#     return redirect(url_for('home'))

# # Artist's route


# @app.route('/artist_profile/<int:artist_id>', methods=['GET'])
# def artist_profile(artist_id):
#     artist = Artist.query.get(artist_id)
#     if artist:
#         return render_template('artist_profile.html', artist=artist)
#     else:
#         # Handle artist not found case
#         return render_template('artist_not_found.html')


# @app.route('/artist_edit_profile/<int:artist_id>', methods=['GET', 'POST'])
# def edit_artist(artist_id):
#     artist = Artist.query.get(artist_id)
#     # if not artist:
#     #     # Handle artist not found case
#     #     return render_template('artist_not_found.html')

#     form = ArtistProfileForm(obj=artist)

#     if form.validate_on_submit():
#         form.populate_obj(artist)
#         db.session.commit()
#         return redirect(url_for('artist', artist_id=artist.artist_id))

#     return render_template('edit_artist.html', form=form, artist=artist)


# @app.route('/artist_delete_profile/<int:artist_id>', methods=['POST'])
# def delete_artist(artist_id):
#     artist = Artist.query.get(artist_id)
#     if not artist:
#         # Handle artist not found case
#         return render_template('artist_not_found.html')

#     db.session.delete(artist)
#     db.session.commit()
#     return redirect(url_for('home'))

# # Admin's Route


# @app.route('/admin_profile/<int:admin_id>', methods=['GET'])
# def admin_profile(admin_id):
#     admin_obj = Admin.query.get(admin_id)
#     if admin_obj:
#         return render_template('admin_profile.html', admin_obj=admin_obj)
#     else:
#         # Handle admin not found case
#         return render_template('admin_not_found.html')


# @app.route('/admin_edit_profile/<int:admin_id>', methods=['GET', 'POST'])
# def edit_admin(admin_id):
#     admin_obj = Admin.query.get(admin_id)

#     # if not admin_obj:
#     #     # Handle artist not found case
#     #     return render_template('admin_not_found.html')

#     form = AdminLoginForm(obj=admin_obj)

#     if form.validate_on_submit():

#         form.populate_obj(admin_obj)
#         db.session.commit()
#         return redirect(url_for('admin_profile', admin_id=admin_obj.admin_id))
#     hide_password = request.args.get('hide_password', False)
#     return render_template('./forms/admin_profile.html', sysadmin=admin_obj, form=form, hide_password=hide_password)


# @app.route('/admin_delete_profile/<int:admin_id>', methods=['POST'])
# def delete_admin(admin_id):
#     admin_obj = Admin.query.get(admin_id)
#     # if not admin_obj:
#     #     # Handle artist not found case
#     #     return render_template('admin_not_found.html')

#     db.session.delete(admin_obj)
#     db.session.commit()
#     return redirect(url_for('home'))


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import render_template, redirect, url_for, request
from config import app, db
from models import Admin, Fan, Artist
from forms import AdminLoginForm,  FanProfileForm, ArtistProfileForm


@app.route('/')
def home(): 
    return render_template('./forms/home.html')


@app.route('/fan_profile', methods=['GET', 'POST'])
def fan_profile():
    fan_obj = Fan.query.first()
    form = FanProfileForm(obj=fan_obj)

    if form.validate_on_submit():
        fan_obj.full_name = form.full_name.data
        fan_obj.phone_number = form.phone_number.data
        fan_obj.email = form.email.data

        if form.password.data:
            fan_obj.password = form.password.data

        db.session.commit()
        # Redirect to the home page after form submission
        return redirect(url_for('fan_profile'))

    hide_password = request.args.get('hide_password', False)
    return render_template('./forms/fan_profile.html', fan=fan_obj, form=form, hide_password=hide_password)


@app.route('/artist_profile', methods=['GET', 'POST'])
def artist_profile():
    artist_obj = Artist.query.first()
    form = ArtistProfileForm(obj=artist_obj)

    if form.validate_on_submit():
        artist_obj.full_name = form.full_name.data
        artist_obj.username = form.username.data
        artist_obj.phone_number = form.phone_number.data
        artist_obj.seeking_description = form.seeking_description.data
        artist_obj.seeking_venue = form.seeking_venue.data
        artist_obj.facebook_link = form.facebook_link.data
        artist_obj.instagram_link = form.instagram_link.data
        artist_obj.email = form.email.data

        if form.password.data:
            artist_obj.password = form.password.data

        db.session.commit()
        # Redirect to the home page after form submission
        return redirect(url_for('artist_profile'))

    hide_password = request.args.get('hide_password', False)
    return render_template('./forms/artist_profile.html', artist=artist_obj, form=form, hide_password=hide_password)



@app.route('/admin_profile', methods=['GET', 'POST'])
def admin_profile():
    admin_obj = Admin.query.first()
    form = AdminLoginForm(obj=admin_obj)
    if form.validate_on_submit():
        admin_obj.first_name = form.first_name.data
        admin_obj.last_name = form.last_name.data
        admin_obj.email = form.email.data
        admin_obj.password = form.password.data
        db.session.commit()
        return redirect(url_for('admin_profile'))
    hide_password = request.args.get('hide_password', False)
    return render_template('./forms/admin_profile.html', sysadmin=admin_obj, form=form, hide_password=hide_password)


@app.route('/delete_account', methods=['POST'])
def delete_account():
    profile_type = request.form.get('profile_type')
    if profile_type == 'admin':
        admin_objt = Admin.query.first()
        db.session.delete(admin_objt)
        db.session.commit()
        return redirect(url_for('home'))
    elif profile_type == 'fan':
        fan_objt = Fan.query.first()
        db.session.delete(fan_objt)
        db.session.commit()
        return redirect(url_for('home'))
    
    elif profile_type == 'fan':
        artist_objt = Artist.query.first()
        db.session.delete(artist_objt)
        db.session.commit()
        return redirect(url_for('home'))
    
def toggle_seeking():
     if request.method == 'POST':
        toggle = request.form.get('toggle')  # Get the value of the toggle button
        if toggle == 'on':
            # Perform filtering and display results
            venue_size = request.form.get('venue_size')
            venue_location = request.form.get('venue_location')
            venue_capacity = request.form.get('venue_capacity')
            
            # Perform filtering based on the selected criteria
            # Query the show table for shows matching the criteria
            # Generate the result and display it
            result = filter_shows(venue_size, venue_location, venue_capacity)
            return render_template('result.html', result=result)
        else:
            # Toggle is off, display default page without seeking privileges
            return render_template('index.html')
     else:
        # Display default page without seeking privileges
        return render_template('index.html')

# Function to filter shows based on selected criteria
def filter_shows(venue_size, venue_location, venue_capacity):
    # Query the show table and filter based on selected criteria
    # Return the filtered shows
    # Example implementation:
    filtered_shows = []
    # Perform the necessary filtering logic on the show table
    # Populate the filtered_shows list with the matching shows
    return filtered_shows


if __name__ == '__main__':
    app.run(debug=True)