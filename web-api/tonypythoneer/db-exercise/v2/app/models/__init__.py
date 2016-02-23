#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""Models

https://flask-migrate.readthedocs.org/en/latest/

The models.py needs to be collected in __init__.py
When manage.py imports it, it must include total modes
and can be detected by Alembic. It ensures
that migrations will migrate on database.
"""
from .users import *
from .devices import *