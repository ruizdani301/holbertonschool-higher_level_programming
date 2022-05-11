#!/usr/bin/python3

"""
    Write a python file that contains the class definition
    of a  city  and an instance  Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
Base = declarative_base()

class City(Base):
    """ Class City"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=True,)
