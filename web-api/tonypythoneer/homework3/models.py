#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20151026
#  @date          20151026
"""urls: models
"""
import datetime
import hashlib
import re

from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    account = Column(String(255), unique=True, index=True)
    password = Column(String(128))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow,
                        default=datetime.datetime.utcnow)

    def __init__(self, account, password):
        self.account = account
        self.password = self._make_password(password)

    def __repr__(self):
        return "<User(account='%s')>" % (self.account)

    '''
    @validates('account')
    def validate_account(self, fieldname, value):
        assert bool(re.match(r"[^@]+@[^@]+\.[^@]+", value))
        return value
    '''

    def _make_password(self, password):
        hashed_password = hashlib.sha1(password).hexdigest()
        return hashed_password

    def set_password(self, password):
        self.password = self._make_password(password=password)

    def check_password(self, password):
        hashed_password = self._make_password(password=password)
        is_correct = self.password is hashed_password
        return is_correct
