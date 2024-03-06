from sqlalchemy import Column, String
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.__init__ import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances"""
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
