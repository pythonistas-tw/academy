import hashlib
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

 
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

