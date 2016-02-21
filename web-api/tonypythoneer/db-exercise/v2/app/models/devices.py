#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160201
#  @date          20160201
#  @version       0.0
"""The model is designed for Devices API
"""
from datetime import datetime

from .. import db
from . import mixins


__all__ = ["Device"]


class Device(db.Model, mixins.CRUDMixin):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    device_type = db.Column(db.String(16), index=True)

    def __init__(self, device_type):
        self.device_type = device_type

    '''
    def __repr__(self):
        return "<User(email='%s')>" % (self.email)
    '''
