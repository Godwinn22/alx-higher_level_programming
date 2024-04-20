#!/usr/bin/python3
"""
This is a python file that contains the class definition of a
State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
# from sqlalchemy.orm import relationship


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The name of the table
        id (int): The id of the state class
        name (str): The name column of the state class
        state_id(int): The the state the cities belong to,
        in relationship
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # state = relationship("State", back_populates="cities")
