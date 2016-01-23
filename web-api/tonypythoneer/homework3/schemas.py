#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160123
#  @date          20160123
"""ModelSchema

Source:
https://marshmallow-sqlalchemy.readthedocs.org/en/latest/#generate-marshmallow-schemas

It's like ModelSerializer of DRF.
http://www.django-rest-framework.org/api-guide/serializers/#modelserializer
"""
from marshmallow_sqlalchemy import ModelSchema

from db_connector import DbConnecter
from models import User


# Call Db session
db_connector = DbConnecter()
Session = db_connector.get_session()


class BaseSchema(ModelSchema):
    class Meta:
        sqla_session = Session


class UserSchema(BaseSchema):

    # Inherit BaseSchema's options
    class Meta(BaseSchema.Meta):
        model = User
