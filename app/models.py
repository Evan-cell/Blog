from . import db

#quote model 
class Quotes: 
  '''Class to display random quotes'''
  def __init__(self,author,quote):
    self.author = author
    self.quote = quote
# db model
    