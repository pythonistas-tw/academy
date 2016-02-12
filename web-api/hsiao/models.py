import hashlib
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, validates

Base = declarative_base()

class User(Base):
	__tablename__ = "User"

	id = Column(Integer, primary_key=True)
	account = Column(String)
	password = Column(String)

	@validates('account')
	def validate_email(self, key, address):
		assert '@' in address
		return address

	def __init__(self, account, password):
		self.account = account
		self.password = hashlib.sha1(password).hexdigest()

	def __repr__(self):
	    return "<User(id='%d', account='%s', password='%s')>" % (self.id, self.account, self.password)

if __name__ == "__main__":
	engine = create_engine("sqlite:///db.sqlite", echo=True)
	Base.metadata.create_all(engine)

	Session = sessionmaker(bind=engine)
	session = Session()

	user_1 = User(account="username1@gmail.com", password="adsdasds".encode('utf-8'))
	print("Mapper:", user_1.__mapper__)
	session.add(user_1)
	row = session.query(User).filter_by(account="username1@gmail.com").first()
	if row:
		print("Found user1")
		print(row)
	else:
		print('Can not find user1')
	session.rollback()
	row = session.query(User).filter_by(account="username1@gmail.com").first()
	if row:
		print("Found user_1 after rollback")
		print(row)
	else:
		print("Can not find user_1 after rollback")

	user_2 = User(account="username2@gmail.com", password="zxczxczxcx".encode('utf-8'))
	session.add(user_1)
	session.add(user_2)
	session.commit()
	affected_rows = session.query(User).filter_by(id=1).delete()
	print("Affected rows:", affected_rows)
	if session.query(User).filter_by(id=1).count() == 0:
		print("id 1 not found")

	user_3 = User(account="username3@gmail.com", password="qweqwewq".encode('utf-8'))
	session.add(user_3)
	print("Before update:")
	for r in session.query(User):
		print(r.id, r.account)
	
	affected_rows = session.query(User).filter_by(id=3).update({"id":5, "password": "sqlalchemy"})
	print("Affected rows:", affected_rows)
	print("After update:")
	for r in session.query(User):
		print(r.id, r.account)
