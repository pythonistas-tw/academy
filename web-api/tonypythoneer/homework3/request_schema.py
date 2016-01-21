#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""request_schema
"""
from marshmallow import Schema, fields


class SignupSchema(Schema):
    account = fields.Email(required=True, location='json')
    password = fields.Str(required=True, location='json')

    class Meta:
        strict = True
