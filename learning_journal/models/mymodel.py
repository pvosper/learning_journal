
"""
Our model will be called an Entry. Here’s what you need to know:
    It should be stored in a database table called entries
    It should have a primary key field called id
    It should have a title field which accepts unicode text up to 255
        characters in length
    The title should be unique and it should be impossible to save an entry
        without a title.
    It should have a body field which accepts unicode text of any length
        (including none)
    It should have a created field which stores the date and time the object
        was created.
    It should have an edited field which stores the date and time the object
        was last edited.
    Both the created and edited field should default to now if not provided
        when a new instance is constructed.
    The entry class should support a classmethod all that returns all the
        entries in the database, ordered so that the most recent entry is
        first.
    The entry class should support a classmethod by_id that returns a single
        entry, given an id.
"""

# from datetime import datetime
# datetime.now().time()

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text) # unique; required
    # SQLite constraints: UNIQUE, NOT NULL, CHECK and FOREIGN KEY
    body = Column(Text)
    created = Column(Text)
    edited = Column(Text)
    # created = Column(os.DateTime, default=func.now())
    # edited = Column(os.DateTime, default=func.now())


Index('my_index', Entry.title, unique=True, mysql_length=255)


# class MyModel(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     value = Column(Integer)


# Index('my_index', MyModel.name, unique=True, mysql_length=255)