from flask import request

from webargs.flaskparser import use_args


def parse_args(schema):
    method_location_map = {
        'GET': 'query',
        'POST': 'json',
        'PUT': 'json',
        'PATCH': 'json',
        'DELETE': 'query',
    }
    location = method_location_map[request.method]

    @use_args(schema, locations=(location,))
    def get_cleaned_args(args):
        return args
    return get_cleaned_args()
