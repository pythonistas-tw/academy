import os

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#declare-a-mapping
# Start to declare model object -- it's addressed as `Base`
Base = declarative_base()


# http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#create-a-schema
# Start to code the fields of the model
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())


# http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#connecting
# Create a sqlite and connect the sql server
db_name = 'sample.sqlite'
if os.path.exists(db_name):
    os.remove(db_name)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///' + db_name)


# http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#creating-a-session
# Create a session with sql server as engine
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)

# http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#create-a-schema
# Register schema and create tables
Base.metadata.create_all(engine)
