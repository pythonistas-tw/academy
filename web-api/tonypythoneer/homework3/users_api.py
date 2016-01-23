#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""main app
"""
from flask import Flask, jsonify, request

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound
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
@use_args(SignupSchema(), locations=('json',))
def signup(args):
    user = User(**args)
    session.add(user)
    try:
        session.commit()
    except IntegrityError as e:
        e.data = user_errors.USER_ERR_1001_REGISTERED_ACC
        raise
    return jsonify({"result": "OK"}), 200


# Function-based views: Get the user
@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(user_id):
    if request.method == 'GET':
        user = session.query(User).filter(User.id == user_id).one()
        print user
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
    if not hasattr(err, "data"):
        return jsonify({
            "error_code": 1,
            "message": "The database schema isn't the newest."
        }), 500
    return jsonify(err.data), 400


if __name__ == '__main__':
    app.run(debug=True)
