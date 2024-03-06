#!/usr/bin/python3

"""Defines the User class."""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.place import Place  # import place conditionally
from models.review import Review

storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """user"""
    __tablename__ = "users"

    if storage_type == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
