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
from error_handlings import user_errors


# Initial process: Initialize Flask app
app = Flask(__name__)

# Call Db session
db_connector = DbConnecter()
session = db_connector.get_session()


# Function-based views: signup
@app.route('/signup', methods=['POST'])
@use_args(SignupSchema())
def signup(args):
    try:
        user = User(**args)
        session.add(user)
        session.commit()
    except IntegrityError as err:
        err.data = user_errors.USER_ERR_1001_REGISTERED_ACC
        raise
    return jsonify({"result": "OK"}), 200


@app.errorhandler(422)
def handle_webargs_abort(err):
    """Receive error from webargs abort

    Let message be more friendly, it will remain the errors as a dictionary format.
        example:
            Orinally, it's like this {'value2': [u'Not a valid number.']}.
            It will convert to {'value2': u'Not a valid number.'}
    """
    msgs = {k: v.pop() for k, v in err.data['messages'].items()}
    return jsonify({
        'error_code': 0,
        'message': "Invalid request could not be understood "
                   "by the server due to malformed syntax.",
        'errors': msgs,
    }), 400


@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy_exception(err):
    """Call customize error handling message from exception data

    return example:
        {
            "error_code": 1001,
            "message": "The account is registered."
        }
    """
    return jsonify(err.data), 400


if __name__ == '__main__':
    app.run(debug=True)
