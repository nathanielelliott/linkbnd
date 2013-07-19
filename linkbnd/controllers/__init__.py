import random
import string
from flask import flash, redirect, url_for, render_template, request, abort
from flask.ext.login import (login_user, logout_user, login_required,
        current_user)
from sqlalchemy.orm.exc import NoResultFound
from linkbnd import app, db, login_manager, flask_bcrypt
from linkbnd.models import User, URLCard
from linkbnd.forms import LoginForm, SettingsForm, NewLinkForm


def flash_errors(form):
    '''
    Flash all form errors.

    Snagged from http://flask.pocoo.org/snippets/12/
    '''
    for field, errors in form.errors.items():
        for error in errors:
            flash('Error in %s - %s' % (
                getattr(form, field).label.text,
                error
            ))

@login_manager.user_loader
def load_user(id):
    try:
        return User.query.filter_by(email=id).one()
    except:
        return None

@app.route('/')
def index():
    cards = URLCard.query.all()
    settings_form = SettingsForm()
    login_form = LoginForm()
    link_form = NewLinkForm()
    return render_template('index.html', cards=cards,
            login_form=login_form, settings_form=settings_form,
            link_form=link_form, user=current_user)

@app.route('/settings/', methods=['POST'])
def settings():
    settings_form = SettingsForm()
    login_form = LoginForm()
    link_form = NewLinkForm()
    if request.method == 'POST':
        if settings_form.validate_on_submit():
            current_user.email = settings_form.email.data
            current_user.password = flask_bcrypt.generate_password_hash(
                    settings_form.password.data)
            db.session.add(current_user)
            db.session.commit()
    flash_errors(settings_form)
    return redirect(url_for('index'))

@app.route('/link/', methods=['POST'])
def newlink():
    pass

@app.route('/login/', methods=['POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            try:
                user = User.query.filter_by(email=login_form.email.data).one()
                if flask_bcrypt.check_password_hash(user.password,
                        login_form.password.data) is True:
                    login_user(user, remember=login_form.remember.data)
                    return redirect(url_for('index'))
            except NoResultFound:
                flash('Invalid login.')
            else:
                flash_errors(login_form)
    return redirect(url_for('index'))

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
