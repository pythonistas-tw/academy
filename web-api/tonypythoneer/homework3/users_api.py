#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""main app
"""
from flask import Flask, jsonify, request, Response, json

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from webargs.flaskparser import use_args

from db_connector import DbConnecter
from models import User
from schemas import UserSchema
from error_handlings import user_errors
from webargs_utils import parse_args


# Initial process: Initialize Flask app
app = Flask(__name__)

# Call Db session
db_connector = DbConnecter()
Session = db_connector.get_session()
session = Session()


# Function-based views: signup
@app.route('/signup', methods=['POST'])
@use_args(UserSchema(), locations=('json',))
def signup(args):
    user = User(**args)
    session.add(user)
    try:
        session.commit()
    except IntegrityError as e:
        e.data = user_errors.USER_ERR_1001_REGISTERED_ACC
        raise
    return Response(response=json.dumps({"result": "OK"}), status=200,
                    mimetype="application/json")


# Function-based views: Get the user
@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(user_id):
    try:
        user = session.query(User).filter(User.id == user_id).one()
    except NoResultFound:
        raise
    if request.method == 'GET':
        schema = UserSchema()
        data = schema.dump(user).data
        return Response(response=json.dumps(data), status=200,
                        mimetype="application/json")
    if request.method == 'PUT':
        args = parse_args(UserSchema(dump_only=("account", "password",)))
        user.nickname = args['nickname'] if args['nickname'] else user.nickname
        session.commit()
        return Response(response=json.dumps({"result": "OK"}), status=200,
                        mimetype="application/json")
    if request.method == 'DELETE':
        session.delete(user)
        session.commit()
        return Response(response=json.dumps({"result": "OK"}), status=200,
                        mimetype="application/json")


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


@app.errorhandler(IntegrityError)
def handle_integrityerror_exception(err):
    """Call customize error handling message from exception data

    return example:
        {
            "error_code": 1001,
            "message": "The account is registered."
        }
    """
    return jsonify(err.data), 400


@app.errorhandler(NoResultFound)
def handle_noresultfound_exception(err):
    """Call customize error handling message from exception data

    return example:
        {
            "message": "Not Found"
        }
    """
    return jsonify({"message": "Not Found"}), 404


@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemyerror_exception(err):
    """
    """
    return jsonify({
        #"error_code": 1,
        "message": err.message,
        "doc": err.__doc__,
        "class_name": err.__class__.__name__
    }), 500


if __name__ == '__main__':
    app.config["JSON_SORT_KEYS"] = False
    app.run(debug=True)
