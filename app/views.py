# pylint: disable=W0312
# pylint: disable=C0111
# pylint: disable=W0611
# pylint: disable=C0303
# pylint: disable=C0301 
# pylint: disable=E1101

import os
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from datetime import date
from app import app, db, login_manager
from app.forms import UserForm
from app.models import UserProfile

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = UserForm()
    if request.method == 'POST':
        fname = form.firstname.data
        lname = form.lastname.data
        email = form.email.data
        gender = form.gender.data
        location = form.location.data
        bio = form.bio.data
        photo = form.file.data
        filename = secure_filename(photo.filename)
        join_date = date.today().strftime("%B %d, %Y")
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Your Profile Has Been Created!', 'success')

        db.session.add(UserProfile(firstname=fname, lastname=lname, email=email, gender=gender, location=location, bio=bio, file=filename, join_date=join_date))
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('profile.html', form=form)

@app.route('/profiles', methods=['GET','POST'])
def profiles():
    model = UserProfile.query.all()
    #print(model)
    return render_template('profiles.html', model=model)

@app.route('/profile/<userid>')
def viewProfile(userid):
    user = UserProfile.query.filter_by(id= int(userid)).first()
    return render_template('user.html', user = user)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
