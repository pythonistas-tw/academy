"""reqparse

http://flask-restful-cn.readthedocs.org/en/0.3.4/api.html#reqparse.Argument
class reqparse.Argument(
    name,
    default=None,
    dest=None,
    required=False,
    ignore=False,
    type=<function <lambda>>,
    location=('json', 'values'),
    choices=(),
    action='store',
    help=None,
    operators=('=', ),
    case_sensitive=True,
    store_missing=True,
    trim=False
)
"""
from application.utils.reqparse_plus import create_parser, email_type


user_parser_fields = [
    dict(name='username',
         type=str,
         required=True),
    dict(name='gender',
         choices=('male', 'female'),
         help='Please select a valid choice: male or female'),
    dict(name='email',
         type=email_type)
]
user_parser = create_parser(user_parser_fields)
