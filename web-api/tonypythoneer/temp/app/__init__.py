from flask import Flask

from config import config


# Example
INSTALL_EXTENSIONS = (
    'sqlalchemy.SQLAlchemy',
)


# Example
INSTALL_BLUEPRINTS = (
    {'blueprint': 'main.main', 'url_prefix': '/'},
)


def install_extensions(flask_app, extensions):
    from flask import ext
    for extension in extensions:
        module_name, instance_name = extension.split('.')
        Module = getattr(ext, module_name)
        Instance = getattr(Module, instance_name)
        instance = Instance()
        instance.init_app(flask_app)


def install_blueprints(flask_app, blueprints):
    import app
    for blueprint in blueprints:
        module_name, instance_name = blueprint['blueprint'].split('.')
        module = getattr(app, module_name)
        instance = getattr(module, instance_name)
        app.register_blueprint(instance)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Install: Install third-party Flask apps
    # install_extensions(flask_app=app, extensions=INSTALL_EXTENSIONS)
    # install_blueprints(flask_app=app, extensions=INSTALL_BLUEPRINTS)

    return app
