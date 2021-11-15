from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile
from .. import db
from ..requests import get_quotes
from flask_login import login_required
from ..models import  User

# Views
@main.route('/',methods = ["GET"])
def  index():
  '''
  Function that returns the home page
  '''
#   blogs_found = Blogs.query.order_by(Blogs.submitted.desc()).all()
  quotes = get_quotes()
  title = "kim blog"
  return render_template('index.html',title = title,quotes = quotes)
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)  