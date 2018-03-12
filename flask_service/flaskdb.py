# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine
# from sqlalchemy.ext.automap import automap_base

# Base = automap_base()

# # engine
# engine = create_engine("sqlite:///../db.sqlite3")
# # reflect the tables
# Base.prepare(engine, reflect=True)

# print Base.classes.Image
# # mapped classes are now created with names by default
# # matching that of the table name.
# Parameter = Base.classes.parameter
# Image = Base.classes.image
# session = Session(engine)

# rudimentary relationships are produced
# session.add(Address(email_address="foo@bar.com", user=User(name="foo")))
# session.commit()

# # collection-based relationships are by default named
# # "<classname>_collection"
# print (u1.address_collection)

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#Create and engine and get the metadata
Base_declare = declarative_base()

# an Engine, which the Session will use for connection
# resources
dbPath = '../db.sqlite3'
engine = create_engine('sqlite:///%s' % dbPath)

Session = sessionmaker(bind=engine,autoflush=False)

#create metadata definition
metadata = MetaData(bind=engine)

# create a Session
session = Session()

class Image(Base_declare):
    __table__ = Table('imagens_image', metadata, autoload=True)

class Parameter(Base_declare):
    __table__ = Table('imagens_parameter', metadata, autoload=True)


# def loadSession():
#     """"""

#     metadata = MetaData(engine)
#     moz_bookmarks = Table('imagens_image', metadata, autoload=True)
#     mapper(Image, moz_bookmarks)
#     moz_bookmarks = Table('imagens_parameter', metadata, autoload=True)
#     mapper(Parameter, moz_bookmarks)

#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session

# session = loadSession()

# if __name__ == "__main__":
#     session = loadSession()
#     res = session.query(Image).all()
#     res[1].title
