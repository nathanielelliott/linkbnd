import os
from linkbnd import db, app, flask_bcrypt
from linkbnd.models import URLCard, User
import linkbnd.config

urls = [
        URLCard(url='http://google.com/', description='A search engine.', title='Google',
                icon_url='http://cdn1.iconfinder.com/data/icons/black-icon-social-media/512/099318-google-logo-square.png'),
        URLCard(url='http://imgur.com',
                description='The simple image sharing service.', title='Imgur',
                icon_url='http://www.skylark95.com/wp-content/uploads/2012/04/Imgur_Logo_Icon_normal.png'),
        URLCard(url='http://trello.com', description='Project management.', title='Trello',
                icon_url='http://harveychamplin.com/flipbook/pages/trello-logo-i2.png'),
        URLCard(url='http://reddit.com', description='Time wasting.', title='Reddit',
                icon_url='http://cdn1.iconfinder.com/data/icons/black-icon-social-media/512/099349-reddit-logo-square.png'),
        URLCard(url='https://facebook.com', description='Social time wasting.', title='Facebook',
                icon_url='http://images2.wikia.nocookie.net/__cb20130408220028/warframe/images/7/78/Facebook_logo(2).png'),
]

os.remove(os.path.join(linkbnd.config._basedir, 'app.db'))
db.create_all()
for url in urls:
    db.session.add(url)
user = User(email='mark@markcaudill.me',
        password=flask_bcrypt.generate_password_hash(u'---P@ssw0rd1--'))
db.session.add(user)
db.session.commit()
app.run(host='0.0.0.0', port=5000, debug=True)
