#!/usr/bin/python3
"""
    Write a python file that contains the class definition
    of a  State  and an instance  Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ class states
    """
    __tablename__ = 'states'

    cities = relationship("City", cascade="all, delete")
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)