from flask import jsonify

from .. import app


__all__ = [
    "handle_notfound",  # 404
    "handle_unauthorized",  # 401
    "handle_unprocessable_entity_by_webargs",  # 422
]


@app.errorhandler(404)
def handle_notfound(err):
    """It's possible to be caused by url or sqlalchemy
    """
    return jsonify({"message": "Not Found"}), 404


@app.errorhandler(401)
def handle_unauthorized(err):
    """It's possible to be caused by login
    """
    return jsonify({"message": "Unauthorized"}), 401


@app.errorhandler(422)
def handle_unprocessable_entity_by_webargs(err):
    msgs = {k: v.pop() for k, v in err.data['messages'].items()}
    return jsonify({
        'message': "Invalid request could not be understood "
                   "by the server due to malformed syntax.",
        'errors': msgs,
    }), 400
    return jsonify(res_data), 400
