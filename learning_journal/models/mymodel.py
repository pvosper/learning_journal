#import stuff used by Entry
import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    )

from .meta import Base

# this is the class that came with the scaffold, we can remove it
# class MyModel(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     value = Column(Integer)
#
#
# Index('my_index', MyModel.name, unique=True, mysql_length=255)

#add entry class - to be used by our learning journal
class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def all(cls, session=None):
        """return a query with all entries, ordered by creation date reversed
        """
        if session is None:
            session = DBSession
        return session.query(cls).order_by(sa.desc(cls.created)).all()

    @classmethod
    def by_id(cls, id, session=None):
        """return a single entry identified by id
        If no entry exists with the provided id, return None
        """
        if session is None:
            session = DBSession
        return session.query(cls).get(id)