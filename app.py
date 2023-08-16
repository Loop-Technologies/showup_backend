from flask import render_template, redirect, url_for, request
# from flask_login import current_user
from config import app, db
from models import Admin, Fan
from forms import AdminLoginForm,  FanProfileForm


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
# @app.route('/fan/profile', methods=['GET'])
# @login_required  # Assuming you have implemented login functionality
# def user_profile():
#     user = current_user  # Fetch the currently authenticated user
#     return render_template('fan_profile.html', fan=fan)


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


if __name__ == '__main__':
    app.run(debug=True)
