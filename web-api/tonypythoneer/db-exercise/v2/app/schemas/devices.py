#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160201
#  @date          20160201
"""schemas

Field classes for various types of data.
    http://marshmallow.readthedocs.org/en/latest/api_reference.html#module-marshmallow.fields

“Read-only” and “Write-only” Fields
    https://marshmallow.readthedocs.org/en/latest/quickstart.html#read-only-and-write-only-fields

Meta
    http://marshmallow.readthedocs.org/en/latest/api_reference.html#marshmallow.Schema.Meta
"""
from marshmallow import Schema, fields, validate


class DeviceSchema(Schema):
    DEVICE_TYPE = (
        'desktop',
        'tablet',
        'mobile',
    )

    device_type = fields.Str(validate=validate.OneOf(choices=DEVICE_TYPE))

    class Meta:
        strict = True
