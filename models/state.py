#!/usr/bin/python3

""" State Module for HBNB project
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class
    Creates a relationship between State (parent) and City (child) classes.
    """
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """getter attribute that returns the list of City instances
            if City.state_id==current State_id
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
# from sqlalchemy import Column, String
# from models.base_model import BaseModel
# from sqlalchemy.orm import relationship
# from models.base_model import Base
# from models.__init__ import storage

# class State(BaseModel, Base):
#     """ State class """
#     __tablename__ = 'states'

#     name = Column(String(128), nullable=False)

#     if storage_type == 'db':
#         cities = relationship("City", backref="state", cascade="all, delete-orphan")
#     else:
#         @property
#         def cities(self):
#             """Getter attribute that returns the list of City instances"""
#             city_list = []
#             for city in storage.all(City).values():
#                 if city.state_id == self.id:
#                     city_list.append(city)
#             return city_list
