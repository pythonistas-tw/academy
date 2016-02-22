#!/usr/bin/env python
# encoding: utf-8


from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms import validators, PasswordField, SubmitField
from wtforms.validators import Required
from models import User

class SignupForm(Form):
    username = TextField("User name",  [validators.Required("Please enter your user name.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Login")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self, session):
        print 'username: ', self.username.data
        print 'password: ', self.password.data
        if not Form.validate(self):
            return None

        user= session.query(User).filter_by(account= str(self.username.data)).first()
        if user:
            if user.check_password(self.password.data):
                return user
            else:
                self.username.errors.append('User/password mismatch')
                return None
        else:
             self.username.errors.append('User/password mismatch')
             return None

