#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""schemas

Field classes for various types of data.
    http://marshmallow.readthedocs.org/en/latest/api_reference.html#module-marshmallow.fields

“Read-only” and “Write-only” Fields
    https://marshmallow.readthedocs.org/en/latest/quickstart.html#read-only-and-write-only-fields

Meta
    http://marshmallow.readthedocs.org/en/latest/api_reference.html#marshmallow.Schema.Meta
"""
from flask import url_for
from flask import request

from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    type = fields.Str(default='users')  # it tags where it's call from api
    id = fields.Int()

    # profile
    account = fields.Email(required=True, validate=validate.Length(max=255))
    password = fields.Str(required=True, validate=validate.Length(min=3, max=128))
    nickname = fields.Str(missing='')

    # timestamp
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    links = fields.Method('get_links')

    class Meta:
        strict = True
        ordered = True
        dump_only = ('type', 'id', 'created_at', 'updated_at', 'links')
        load_only = ('password',)

    def get_links(self, obj):
        self_url = url_for('.user_detail', user_id=obj.id, _external=True)
        return self_url
