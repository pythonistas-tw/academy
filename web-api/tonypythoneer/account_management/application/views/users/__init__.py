from flask import Blueprint

from . import auth

# Blueprint app initiation:
#     Declare this view as flask branch/blueprint app and extend its route
users_bp = Blueprint('users', __name__)


users_bp.add_url_rule('/me', 'me', auth.me)