import hashlib
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    account = Column(String)
    password = Column(String)

    @validates('account')
    def validate_email_format(self, key, account):
        assert '@' in account
        return account

    def __init__(self, account, password):
        self.account = account
        self.password = hashlib.sha1(password).hexdigest()

    def __repr__(self):
        return "User('%s', '%s')" % \
        (self.account, self.password)

    def check_password(self, password):
        if hashlib.sha1(password).hexdigest() == self.password:
            return True
        else:
            return False

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

