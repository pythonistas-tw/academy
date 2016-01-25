#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""schemas
"""
from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id = fields.Int()

    account = fields.Email(required=True, validate=validate.Length(max=255))
    password = fields.Str(required=True, validate=validate.Length(min=3, max=128))
    nickname = fields.Str(missing='')

    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    class Meta:
        """Meta

        http://marshmallow.readthedocs.org/en/latest/api_reference.html#marshmallow.Schema.Meta
        """
        strict = True
        # Tuple or list of fields to exclude from deserialization.
        # You can consider that as : json.loads(data, excludes=(...,))
        dump_only = ('id', 'created_at', 'updated_at',)
        # Tuple or list of fields to exclude from serialized results.
        # # You can consider that as : json.dumps(data, excludes=(...,))
        load_only = ('password',)
