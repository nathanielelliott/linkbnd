import time
from linkbnd import app, db

class URLCard(db.Model):
    '''
    The model for all URLCard data.
    '''
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.Integer, default=time.time)
    url = db.Column(db.Unicode(2048), nullable=False)
    title = db.Column(db.UnicodeText, nullable=False)
    description = db.Column(db.UnicodeText)
    icon_url = db.Column(db.Unicode(2048))
