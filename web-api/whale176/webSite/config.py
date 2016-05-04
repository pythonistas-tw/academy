import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'qwrtgawrwiulathgaa[9304uPU()$RU#(W}TU($){T$'

basedir = os.path.abspath((os.path.dirname(__file__)))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
