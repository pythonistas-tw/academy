from flask_restful import Resource, marshal_with, abort

from .request_parsers import user_parser
from .response_fields import user_fields

USERS = {
    'Tony': {'username': 'Tony', 'gender': 'male', 'email': 'tony@example.com'},
    'John': {'username': 'John', 'gender': 'male', 'email': 'john@example.com'},
    'Tely': {'username': 'Tely', 'gender': 'male', 'email': 'tely@example.com'},
}


class UserListResource(Resource):
    request_class = user_parser

    def get(self):
        return {'list': USERS}, 200

    def post(self):
        args = self.request_class.parse_args()
        new_id = args['username']
        USERS[new_id] = args
        return None, 201


class UserDetailResource(Resource):
    request_class = user_parser

    def get_object(self, id):
        user = USERS.get(id, '')
        if not user:
            abort(400, message="Client requested a URI that doesn't map to any resource.")
        return user

    @marshal_with(user_fields)
    def get(self, id):
        user = self.get_object(id)
        return user, 200

    def put(self, id):
        user = self.get_object(id)
        args = self.request_class.parse_args()
        USERS[id].update(args)
        return None, 200

    def delete(self, id):
        user = self.get_object(id)
        del USERS[id]
        return None, 204
