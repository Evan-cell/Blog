from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quotes
from flask_login import login_required

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