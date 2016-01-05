from flask_restful import fields


user_fields = {
    'id': fields.Integer,
    'username': fields.String
}

user_list_fields = {
    'list': fields.List(fields.Nested(user_fields)),
}
