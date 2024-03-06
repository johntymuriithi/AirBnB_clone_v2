#!/usr/bin/python3

""" Place Module for HBNB project
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.review import Review
from models.amenity import Amenity

storage_type = getenv("HBNB_TYPE_STORAGE")

place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel):

    """ A place to stay
    """
    __tablename__ = "places"

    if storage_type == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
            with place_id equals to the current Place.id
            """
            return [review for review in models.storage.all(Review)
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute amenities for FileStorage"""
            list_amenities = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.place_id == self.amenity_ids:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute amenities for FileStorage"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
