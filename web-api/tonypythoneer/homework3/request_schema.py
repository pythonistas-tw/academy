#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""request_schema
"""
from marshmallow import Schema, fields, validate


class SignupSchema(Schema):
    account = fields.Email(required=True, validate=validate.Length(max=10))
    password = fields.Str(required=True, validate=validate.Range(min=3, max=6))
    nickname = fields.Str()

    class Meta:
        strict = True
