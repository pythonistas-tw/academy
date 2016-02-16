from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import PasswordType
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import validates
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    uid = Column(Integer, primary_key=True)
    account = Column(String, nullable=False)
    password = Column(PasswordType(schemes=['sha1_crypt']), nullable=False)

    @validates('account')
    def validate_account(self, key, email):
        assert '@' in email, "Account format isn't correct! (Correct sample: default@gmail.com)"
        return email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.uid)

    def __repr__(self):
        return "<User(uid={}, account={})>".format(self.uid, self.account)

class DBUse():
    def __init__(self):
        self.engine = create_engine('sqlite:///mydb.sqlite', echo=False)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def f_create(self, account=None, password=None):
        if account and password:
            count = self.session.query(User).filter_by(account=account).count()
            if count > 0:
                assert False, "Account has already used."
            print ("Create User:")
            new_user = User(account=account, password=password)
            self.session.add(new_user)
            self.session.commit()
            print ("ID #{}, Account {}".format(new_user.uid, new_user.account))
        else:
            assert False, "User creation fails, 'Account' and 'Password' cannot be Null."

    def f_read(self, uid=None, account=None):
        if (not uid) and (not account):
            result = self.session.query(User).all()
            print ("Read All Users:")
            for i in result:
                print ("ID #{}, Account {}".format(i.uid, i.account))
            return result
        elif uid and account:
            try:
                result = self.session.query(User).filter_by(uid=uid).filter_by(account=account).one()
            except NoResultFound:
                assert False, "User Not Found by ID #{} and Account {}.".format(uid, account)
            print ("Read One User by ID and Account:")
            print ("ID #{}, Account {}".format(result.uid, result.account))
            return result
        elif uid:
            try:
                result = self.session.query(User).filter_by(uid=uid).one()
            except NoResultFound:
                assert False, "User Not Found by ID #{}.".format(uid)
            print ("Read One User by ID:")
            print ("ID #{}, Account {}".format(result.uid, result.account))
            return result
        else:
            result = self.session.query(User).filter_by(account=account).all()
            print ("Read All Users by Account:")
            for i in result:
                print ("ID #{}, Account {}".format(i.uid, i.account))
            return result

    def f_login(self, account=None, password=None):
        if account and password:
            try:
                result = self.session.query(User).filter_by(account=account).one()
                if result.password == password:
                    return result
            except NoResultFound:
                return None
            return None

    def f_update(self, user=None, account=None, password=None):
        if not user:
            assert False, "User Not Found."
        uid = user.uid
        if account and password:
            user.account = account
            user.password = password
            self.session.commit()
            print ("Update Account and Password:")
            new_user = self.session.query(User).filter_by(uid=uid).one()
            print ("ID #{}, Account {}".format(new_user.uid, new_user.account))
        elif account:
            user.account = account
            self.session.commit()
            print ("Update Account:")
            new_user = self.session.query(User).filter_by(uid=uid).one()
            print ("ID #{}, Account {}".format(new_user.uid, new_user.account))
        elif password:
            user.password = password
            self.session.commit()
            print ("Update Password:")
            new_user = self.session.query(User).filter_by(uid=uid).one()
            print ("ID #{}, Account {}".format(new_user.uid, new_user.account))
        else:
            print ("Nothing need to be updated.")

    def f_delete(self, user=None):
        if not user:
            assert False, "User Not Found."
        print ("Delete User:")
        print ("ID #{}, Account {}".format(user.uid, user.account))
        self.session.delete(user)
        self.session.commit()