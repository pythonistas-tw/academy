#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20151222
#  @date          20151222
"""Numeric Expression
"""
import operator

from flask import Flask, jsonify, request

from flask_wtf import Form
from wtforms import FloatField


app = Flask(__name__)


class NumericExpressionForm(Form):
    """NumericExpressionForm"""
    value1 = FloatField('value1')
    value2 = FloatField('value2')

    def make_result(self, op):
        """Call op function to do calculate"""
        value1 = self.data.get('value1')
        value2 = self.data.get('value2')
        return op(value1, value2)


class BadReqestException(Exception):
    """BadReqestException"""
    def __init__(self, message):
        """init"""
        Exception.__init__(self)
        self.message = message
        self.status_code = 400


def get_form(form_class, raw_data):
    form = form_class(raw_data, csrf_enabled=False)
    if not form.validate():
        raise BadReqestException(form.errors)
    return form


@app.errorhandler(BadReqestException)
def handle_invalid_usage(error):
    response = jsonify(error.message)
    response.status_code = error.status_code
    return response


@app.route('/sum', methods=['GET'])
def sum():
    # Validation process
    form = get_form(NumericExpressionForm, request.args)
    # Data process
    result = form.make_result(operator.add)
    return jsonify(**{'result': result}), 200


@app.route('/minus', methods=['GET'])
def minus():
    # Validation process
    form = get_form(NumericExpressionForm, request.args)
    # Data process
    result = form.make_result(operator.sub)
    return jsonify(**{'result': result}), 200


@app.route('/multiply', methods=['GET'])
def multiply():
    # Validation process
    form = get_form(NumericExpressionForm, request.args)
    # Data process
    result = form.make_result(operator.mul)
    return jsonify(**{'result': result}), 200


@app.route('/divide', methods=['GET'])
def divide():
    # Validation process
    form = get_form(NumericExpressionForm, request.args)
    # Data process
    result = form.make_result(operator.div)
    return jsonify(**{'result': result}), 200


if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0')
