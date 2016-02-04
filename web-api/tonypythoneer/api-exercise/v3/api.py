#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160106
#  @date          201601
"""Numeric Expression
"""
from flask import Flask, jsonify

from marshmallow import Schema, fields
from webargs.flaskparser import use_args


# Initial process: Initialize Flask app
app = Flask(__name__)


# Reqeust format: This is a numeric expression
## type1: Build a variable with argument fields
req_args = {
    'value1': fields.Float(required=True, location='query'),
    'value2': fields.Float(required=True, location='query')
}
# https://marshmallow.readthedocs.org/en/latest/api_reference.html#module-marshmallow.fields
## type2: Build a class with argument fields
class OperandSchema(Schema):
    value1 = fields.Float(required=True, location='query')
    value2 = fields.Float(required=True, location='query')

    class Meta:
        strict = True


# Function-based views: Sum
@app.route('/sum', methods=['GET'])
@use_args(OperandSchema())
def sum(args):
    result = args['value1'] + args['value2']
    return jsonify({"result": result}), 200


@app.errorhandler(422)
def handle_webargs(err):
    # Data process: field name with error message
    #   example: Orinally, it's like this {'value2': [u'Not a valid number.']}.
    #            It will convert to {'value2': u'Not a valid number.'}
    msgs = { k:v.pop() for k,v in err.data['messages'].items()}
    return jsonify({
        'error_code': 0,
        'message': "Invalid request could not be understood "
                   "by the server due to malformed syntax.",
        'errors': msgs,
    }), 400


if __name__ == '__main__':
    app.run(debug=True)
