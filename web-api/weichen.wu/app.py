from flask import Flask, render_template, redirect, url_for, request
from flask import flash, session

from flask.ext.wtf import Form
from flask.ext.login import LoginManager, current_user, login_required, login_user, logout_user
from flask_wtf.csrf import CsrfProtect
from wtforms import TextField, BooleanField, PasswordField, validators

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.update(
    DEBUG=True,
    SECRET_KEY='0dsuefce3dxc'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
db.init_app(app)


CsrfProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)


class LoginForm(Form):
  username = TextField('Username')
  password = PasswordField('Password')
