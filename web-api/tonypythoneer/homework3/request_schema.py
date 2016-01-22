#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""request_schema
"""
from marshmallow import Schema, fields, validates


from validators import validate_max_length, validate_min_length


class SignupSchema(Schema):
    account = fields.Email(required=True, location='json')
    password = fields.Str(required=True, location='json')
    nickname = fields.Str(location='json')

    class Meta:
        strict = True

    @validates('account')
    def validate_account(self, value):
        validate_max_length(value, max_length=255)

    @validates('password')
    def validate_account(self, value):
        validate_min_length(value, min_length=3)

    @validates('nickname')
    def validate_nickname(self, value):
        if value:
            validate_max_length(value, max_length=255)
