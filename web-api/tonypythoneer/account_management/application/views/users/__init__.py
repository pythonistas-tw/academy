from flask import Blueprint
from flask_restful import Api

from . import auth

# Blueprint app initiation:
#     Declare this view as flask branch/blueprint app and extend its route
users_bp = Blueprint('users', __name__)
users_api = Api(users_bp)

#users_api.add_resource(auth.me, '')
users_api.add_resource(auth.UserListResource, '')
users_api.add_resource(auth.UserDetailResource, '/<id>')
