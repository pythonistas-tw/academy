from flask import Flask

from application import views

# Main app initiation:
#     Initiate this application as flask main app
app = Flask(__name__)

# Route register:
#     Set views (flask branch/blueprint apps) to register_blueprint
#     and start the urls.
app.register_blueprint(views.users.resource_urls, url_prefix='/users')
