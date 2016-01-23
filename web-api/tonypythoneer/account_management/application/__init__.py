from flask import Flask

from .views.users import users_bp

# Main app initiation:
#     Initiate this application as flask main app
app = Flask(__name__)

# Route register:
#     Set views (flask branch/blueprint apps) to register_blueprint
#     and start the urls.
app.register_blueprint(users_bp, url_prefix='/users')
