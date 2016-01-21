#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""main app
"""
from flask import Flask, jsonify

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from webargs.flaskparser import use_args

from db_connector import DbConnecter
from models import User
from request_schema import SignupSchema


# Initial process: Initialize Flask app
app = Flask(__name__)

# Call Db session
db_connector = DbConnecter()
session = db_connector.get_session()


# Function-based views: signup
@app.route('/signup', methods=['POST'])
@use_args(SignupSchema())
def signup(args):
    user = User(**args)
    session.add(user)
    session.commit()
    return jsonify({"result": "OK"}), 200


@app.errorhandler(422)
def handle_webargs(err):
    # Data process: field name with error message
    #   example: Orinally, it's like this {'value2': [u'Not a valid number.']}.
    #            It will convert to {'value2': u'Not a valid number.'}
    msgs = {k: v.pop() for k, v in err.data['messages'].items()}
    return jsonify({
        'error_code': 0,
        'message': "Invalid request could not be understood "
                   "by the server due to malformed syntax.",
        'errors': msgs,
    }), 400


@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy(err):
    print err
    print dir(err)
    #msgs = {k: v.pop() for k, v in err.data['messages'].items()}
    return jsonify({
        'error_code': 0,
        'message': "Invalid request could not be understood "
                   "by the server due to malformed syntax.",
        'errors': "fuck",
    }), 400


if __name__ == '__main__':
    app.run(debug=True)
