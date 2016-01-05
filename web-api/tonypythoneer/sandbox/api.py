#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20151222
#  @date          20151222
"""Abort test
"""
from flask import Flask, abort, jsonify


app = Flask(__name__)


@app.errorhandler(400)
def error400(e):
    response = jsonify(**{'message': 'Bad Request'})
    return response, 400


@app.route("/test")
def view():
    abort(400)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
