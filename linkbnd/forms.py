from linkbnd import app
from flask.ext.wtf import (Form, TextField, PasswordField, BooleanField,
        TextAreaField, Required, Email, URL, FileField, EqualTo)


class LoginForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember Me', validators=[Required()],
            default=True)


class NewLinkForm(Form):
    url = TextField('URL', validators=[Required(), URL()])
    title = TextField('Title', validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    image = FileField('Image', validators=[Required()])


class SettingsForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('New Password', validators=[
        Required(), EqualTo('confirm', message='Passwords must match.')
    ])
    confirm = PasswordField('Confirm', validators=[Required()])
