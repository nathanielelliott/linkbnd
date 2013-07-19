from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
import linkbnd.config


app = Flask(__name__)
app.config.from_object('linkbnd.config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
flask_bcrypt = Bcrypt(app)

from linkbnd.controllers import *
