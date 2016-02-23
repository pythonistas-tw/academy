#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""The model is designed for Users API

Security Helpers about werkzeug with generate_password_hash and check_password_hash:
    http://werkzeug.pocoo.org/docs/0.11/utils/#module-werkzeug.security
"""
from datetime import datetime, timedelta
import random

from flask import jsonify

from flask.ext.login import UserMixin, make_secure_token

from werkzeug.security import generate_password_hash, check_password_hash

from . import mixins
from .. import db, login_manager


__all__ = ["User", "Token"]


class User(UserMixin, mixins.CRUDMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    # profile fields
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(128))
    nickname = db.Column(db.String(255))

    # timestamp fields
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationship
    devices = db.relationship('Device', backref='device', lazy='dynamic')

    # Token relation fields
    last_login = db.Column(db.DateTime)
    token = db.relationship("Token", uselist=False, backref="token")

    def __init__(self, email, password, nickname=None):
        self.email = email
        self.password = generate_password_hash(password)
        self.nickname = email or nickname

    def __repr__(self):
        return "<User(email='%s')>" % (self.email)

    @classmethod
    def authenticate(cls, email=None, password=None):
        """Get the user"""
        user = cls.query.filter_by(email=email).first()
        if not user:
            return None
        if not user.check_password(password):
            return None
        return user

    def set_password(self, password):
        """The default method is sha1 to hash password"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verify password"""
        return check_password_hash(self.password, password)

    def login(self):
        self.last_login = datetime.utcnow()
        # Update token
        if self.token:
            self.token.update()
            return self.token.key
        # Create token
        token = Token(user_id=self.id)
        token.add()
        return self.token.key


    def logout(self):
        if self.token:
            self.token.delete()

    def is_expired(self):
        return self.token.is_expired()


class Token(mixins.CRUDMixin, db.Model):
    __tablename__ = 'token'
    AUTH_TOKEN_DURATION = 60*60

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, index=True)
    key = db.Column(db.String(128), unique=True, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, user_id):
        self.user_id = user_id

    def generate_key(self):
        """Using make_secure_token

        https://flask-login.readthedocs.org/en/latest/_modules/flask_login.html#make_secure_token
        """
        key = make_secure_token(str(self.user_id), key=str(random.random()))
        self.key = key

    def is_expired(self):
        """Check expired"""
        diff = datetime.utcnow() - self.updated_at
        is_expired = diff > timedelta(seconds=self.AUTH_TOKEN_DURATION)
        return is_expired

    def add(self):
        """It's Create of CRUD."""
        self.generate_key()
        db.session.add(self)
        db.session.commit()

    def update(self):
        """It's Create of CRUD."""
        self.generate_key()
        db.session.commit()


@login_manager.request_loader
def load_request(request):
    # Request process: Get token from Authorization of headers
    auth_token = request.headers.get('Authorization', '')
    if not auth_token:
        return None

    # Model process: Get user by token
    user = User.query.filter(Token.key == auth_token).first()
    if not user:
        return None

    # Validation process: The token is expired or not
    if user.is_expired():
        user.token.delete()
        return None

    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return jsonify({"message": "Unauthorized"}), 401
