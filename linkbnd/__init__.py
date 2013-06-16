from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import linkbnd.config

app = Flask(__name__)
app.config.from_object('linkbnd.config')
db = SQLAlchemy(app)

from linkbnd.controllers.index import index
