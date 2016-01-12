from flask_restful import reqparse, inputs


def create_parser(fields):
    parser = reqparse.RequestParser(bundle_errors=True)
    for field in fields:
        parser.add_argument(**field)
    return parser

email_type = inputs.regex("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$")
