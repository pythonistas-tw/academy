#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160122
#  @date          20160122
"""Make customize validators

.. _Reference:
    https://docs.djangoproject.com/en/1.9/ref/validators/
"""
from marshmallow import ValidationError


def validate_min_length(value, min_length):
    """Length must not be greater than %(min_length)s."""
    message = "Length must be greater than %s."
    if len(value) < min_length:
        raise ValidationError(message % min_length)


def validate_max_length(value, max_length):
    """Length must not be greater than %(max_length)s."""
    message = "Length must not be greater than %s."
    if len(value) > max_length:
        raise ValidationError(message % max_length)
