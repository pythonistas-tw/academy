from app import db
from werkzeug import generate_password_hash, check_password_hash


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    pwdhash = db.Column(db.String(54))
    email = db.Column(db.String(120), index=True, unique=True)

    def qry_username(self):
        user = User.query.filter_by(username=self.username.data).first()
        # try:
        return user  # python 3
        # except NameError:
        #     return unicode(self.id)  # python 2

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email, password):
        self.username = username
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
