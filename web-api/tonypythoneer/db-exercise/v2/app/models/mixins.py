#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""The mixins are designed for models
"""
from .. import db


class CRUDMixin(object):
    """Simplify leveraging database"""

    def add(self):
        """It's Create of CRUD."""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """It's Update of CRUD."""
        db.session.commit()

    def delete(self):
        """It's Delte of CRUD."""
        db.session.delete(self)
        db.session.commit()
