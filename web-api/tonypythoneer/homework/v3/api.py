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

'''
# Function-based views: test
@app.route('/test/<int:fuck>', methods=['GET'])
def test(fuck):
    return jsonify({"fuck": fuck}), 200


# Function-based views: test2
@app.route('/test2/<int:fuck>', methods=['GET'])
@use_args({'num': fields.Int(required=True, location='query')})
def test2(args, fuck):
    return jsonify({"fuck": fuck}), 200

@app.route('/user/<int:uid>')
@use_args({'per_page': fields.Int()})
def user_detail(args, uid):
    return ('The user page for user {uid}, '
            'showing {per_page} posts.').format(uid=uid,
                                                per_page=args['per_page'])
'''

@app.errorhandler(422)
def handle_bad_request_by_webargs(err):
    # webargs attaches additional metadata to the `data` attribute
    data = getattr(err, 'data')
    messages = data['exc'].messages if data else ['Invalid request']
    return jsonify({
        'error_code': 0,
        'message': "Invalid request could not be understood "
                   "by the server due to malformed syntax.",
        'errors': messages,
    }), 400


if __name__ == '__main__':
    app.run(debug=True)
