#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160101
#  @date          20160101
"""Numeric Expression
"""
from flask import Flask, make_response, json
from flask_restful import Api, Resource, reqparse, fields, marshal_with


# Initial process: Initialize Flask app
app = Flask(__name__)
api = Api(app)  # Install flask_restful

# Reqeust format: This is a numeric expression
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('value1', type=float, required=True, location='args')
parser.add_argument('value2', type=float, required=True, location='args')

# Response format: This is a output format
resource_fields = {
    'result': fields.Float,
}


# View class: Sum
class Sum(Resource):
    """value1 + value2"""
    @marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        result = args['value1'] + args['value2']
        return {'result': result}, 200


# View class: Minus
class Minus(Resource):
    """value1 - value2"""
    @marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        result = args['value1'] - args['value2']
        return {'result': result}, 200


# View class: Multiply
class Multiply(Resource):
    """value1 * value2"""
    @marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        result = args['value1'] * args['value2']
        return {'result': result}, 200


# View class: Divide
class Divide(Resource):
    """value1 / value2"""
    @marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        result = args['value1'] / args['value2']
        return {'result': result}, 200

# Response representation
@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


# Router process: Resgister views in urls
api.add_resource(Sum, '/sum')
api.add_resource(Minus, '/minus')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')


if __name__ == '__main__':
    app.run(debug=True)
