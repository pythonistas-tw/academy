import os

from flask.ext.script import Manager
from flask.ext.migrate import Migrate

from app import create_app, db, models
import scripts


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


if __name__ == "__main__":
    manager.run(scripts.COMMANDS)
