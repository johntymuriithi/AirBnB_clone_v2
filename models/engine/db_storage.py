#!/usr/bin/python3

"""This module defines the DBStorage class for HBNB
"""

import os
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Creates a new instance of DBStorage
        """

        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env_var = os.environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        try:
            if env_var == 'test':
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        """Query on the current database session (self.__session)
        """

        classes = [User, State, City, Amenity, Place, Review]
        objs = {}

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            for obj in self.__session.query(cls).all():
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return objs

    def new(self, obj):
        """Add the object to the current database session
        """

        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None
        """

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database
        and create the current database session
        """

        Base.metadata.create_all(self.__engine, checkfirst=False)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Method to close the session
        """

        self.__session.close()
