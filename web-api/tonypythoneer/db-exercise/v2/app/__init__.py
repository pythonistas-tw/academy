#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""Init flask app
"""
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.marshmallow import Marshmallow
from flask.ext.login import LoginManager
import configs


# Initializing process: This package is main flask app
app = Flask(__name__)
app.config.from_object(configs.CONFIGS['default'])


# Initializing process: This extesion list is created extension object
db = SQLAlchemy()
ma = Marshmallow()

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'users.login'


def init_extensions(app):
    '''Initializing the flask app with extensions'''
    # Extension List: Wrap up the all extensions
    extensions = (
        db,
        ma,  # Warning: Flask-SQLAlchemy must be initialized before Flask-Marshmallow.
        login_manager,
    )

    # Initializing process: Start to initial each extension
    for extension in extensions:
        extension.init_app(app)


def init_blueprints(app):
    '''Initializing the flask app with blueprints'''
    # Blueprint source: Import the blueprints and note these sources
    from .views import users

    # Blueprint List: Wrap up the all blueprints
    buleprints = (
        dict(blueprint=users.users_bp, url_prefix='/users'),
    )

    # Initializing process: Start to initial each blueprint
    for blueprint in buleprints:
        app.register_blueprint(**blueprint)


def init_error_handlers(app):
    '''import error handler function'''
    from .error_handlers.built_in_exception_handlers import *
    from .error_handlers.status_code_handlers import *
    from .error_handlers.sqlachelmy_handlers import *


def create_app():
    '''It's a factory.'''
    # Initializing process: Initializing the main flask app with extensions
    init_extensions(app)

    # Initializing process: Initializing the main flask app with blueprints
    init_blueprints(app)

    # Initializing process: import error handlers
    init_error_handlers(app)

    return app
