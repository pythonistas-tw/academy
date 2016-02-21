from flask import jsonify

from .. import app


__all__ = [
    "handle_notimplementederror",
]

@app.errorhandler(NotImplementedError)
def handle_notimplementederror(err):
    """Execute query but it doesn't find the data
    """
    return jsonify({"message": err.message}), 500
