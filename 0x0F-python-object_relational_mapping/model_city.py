#!/usr/bin/python3

"""
  contains a base and city class.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer


Base = declarative_base()


class City(Base):
    """
        City class inherits the Base class
        Attributes:
            id (int)
            name (string)
            state_id (string)
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
