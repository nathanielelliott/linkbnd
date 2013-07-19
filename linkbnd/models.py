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


class User(db.Model):
    '''
    Users
    '''
    email = db.Column(db.Unicode(256), primary_key=True)
    password = db.Column(db.Unicode(128))

    # flask-login stuff
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email
