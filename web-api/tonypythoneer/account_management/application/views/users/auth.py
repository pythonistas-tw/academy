from flask_restful import Resource, marshal_with

from .response_fields import user_list_fields

USER_LIST = [
    {'id': 1, 'username': 'Tony'},
    {'id': 2, 'username': 'John'},
    {'id': 3, 'username': 'Tom'},
]

class me(Resource):
    def get(self):
        return 'fuck'

class UserListResource(Resource):
    @marshal_with(user_list_fields)
    def get(self):
        return {'list': USER_LIST}, 200


class UserDetailResource(Resource):
    #@marshal_with(user_list_fields, envelope='list')
    def get(self, id):
        return id, 200

    '''
    def post(self):
        return USER_LIST, 200
    '''
