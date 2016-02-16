from flask import jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from .. import app


__all__ = [
    "handle_integrityerror_exception",
    "handle_noresultfound_exception",
]


@app.errorhandler(IntegrityError)
def handle_integrityerror_exception(err):
    """Execute insert but the data has duplicate index

    return example:
        {
            "error_code": 1001,
            "message": "The account is registered."
        }
    """
    return jsonify(err.data), 409


@app.errorhandler(NoResultFound)
def handle_noresultfound_exception(err):
    """Execute query but it doesn't find the data

    return example:
        {
            "message": "Not Found"
        }
    """
    return jsonify({"message": "Not Found"}), 404
