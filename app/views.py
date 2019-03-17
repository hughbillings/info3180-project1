from app import app,db
from flask import render_template, request, redirect, url_for, flash
from app.forms import UploadForm
from app.models import UserProfile
import os
from werkzeug.utils import secure_filename
import datetime



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/profile', methods=['GET','POST'])
def profile():
    form = UploadForm()
    if request.method == "POST" and form.validate_on_submit():
        firstname = form.fname.data
        lastname = form.lname.data
        gender = form.gender.data
        location = form.location.data
        email = form.email.data
        biography = form.biography.data
        photograph =  form.file.data
        filename = secure_filename(photograph.filename)
        photograph.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user_date = datetime.datetime.today().strftime('%Y-%m-%d')
        user = UserProfile(firstname,lastname,gender,location,biography,filename,email,user_date)
        db.session.add(user)
        db.session.commit()
        flash("Profile Created Successfully")
        return redirect(url_for('profiles'))
    flash_errors(form)
    return render_template('profile.html',form=form)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/profiles')
def profiles():
    users = UserProfile.query.all()
    return render_template("profilelist.html",user=users)
    
@app.route('/profile/<userid>')
def profileview(userid):
   user = UserProfile.query.filter_by(id=userid).first()
   if user is not None:
        return render_template('profileview.html',user=user)
   else:
        flash('Username or Password is incorrect.', 'danger')
        return redirect(url_for('profiles'))
    
    
    