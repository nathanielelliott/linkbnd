from flask import render_template
from linkbnd import app, db
from linkbnd.models import URLCard

@app.route('/')
def index():
    cards = URLCard.query.all()

    return render_template('index.html', cards=cards)
