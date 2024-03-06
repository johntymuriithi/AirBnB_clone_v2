#!/usr/bin/python3

""" City Module for HBNB project
"""

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    """
    __tablename__ = 'cities'

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        # Import Place model conditionally
        from models.place import Place
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""
# from sqlalchemy import Column, String, ForeignKey
# from models.base_model import BaseModel
# from sqlalchemy.orm import relationship
# from models.base_model import Base

# class City(BaseModel, Base):
#     """ The city class, contains state ID and name """
#     __tablename__ = 'cities'

#     name = Column(String(128), nullable=False)
#     state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

#     state = relationship("State", back_populates="cities")

