#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160118
#  @date          20160118
"""Pratice template
"""
import operator

from flask import Flask, render_template, abort

from marshmallow import Schema, fields
from webargs.flaskparser import use_args


app = Flask(__name__)


# Request schema
class OperandSchema(Schema):
    value1 = fields.Float(required=True, location='query')
    value2 = fields.Float(required=True, location='query')
    op = fields.Str(required=True, location='query')

    class Meta:
        strict = True


# Render format
def make_result_msg(value1, value2, op):
    op_dict = {'sum': {'op': '+', 'func': 'add'},
               'minus': {'op': '-', 'func': 'sub'},
               'multiply': {'op': '*', 'func': 'mul'},
               'divide': {'op': '/', 'func': 'div'}}
    if op not in op_dict:
        abort(400)

    
    sign_func_dict = op_dict[op]
    op_sign = sign_func_dict['op']
    op_func = getattr(operator, sign_func_dict['func'])
    msg_element = {
        'value1': value1,
        'value2': value2,
        'op': op_sign,
        'result': op_func(value1, value2)
    }
    msg_format = "The Answer of %(value1)s %(op)s %(value1)s is %(result)s"
    return msg_format % msg_element


# Function-based views: count
@app.route('/count', methods=['GET'])
@use_args(OperandSchema())
def sum(args):
    msg = make_result_msg(**args)
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
