#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20151026
#  @date          20151026
"""urls: models
"""
import datetime
import hashlib
# import re

from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import validates


Base = declarative_base()


def make_default_nickname(account):
    """Fetch name of account as nickname"""
    default_nickname, _ = account.split('@')
    return default_nickname


def make_password(password):
    """Using sha1 to hash password"""
    hashed_password = hashlib.sha1(password).hexdigest()
    return hashed_password


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    # profile fields
    account = Column(String(255), unique=True, index=True)
    password = Column(String(128))
    nickname = Column(String(255))

    # timestamp fields
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow,
                        default=datetime.datetime.utcnow)

    def __init__(self, account, password, nickname=None):
        self.account = account
        self.password = make_password(password)
        self.nickname = nickname if not nickname else make_default_nickname(account)

    def __repr__(self):
        return "<User(account='%s')>" % (self.account)

    def set_password(self, password):
        """Using hash lib to hash password"""
        self.password = make_password(password=password)

    def check_password(self, password):
        """check password"""
        hashed_password = make_password(password=password)
        is_correct = self.password is hashed_password
        return is_correct
