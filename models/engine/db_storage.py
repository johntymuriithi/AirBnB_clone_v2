import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import *

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(os.environ['HBNB_MYSQL_USER'],
                                             os.environ['HBNB_MYSQL_PWD'],
                                             os.environ['HBNB_MYSQL_HOST'],
                                             os.environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session """
        objs_dict = {}
        if cls:
            objs = self.__session.query(eval(cls)).all()
        else:
            all_classes = [User, State, City, Amenity, Place, Review]
            for cls in all_classes:
                objs += self.__session.query(cls).all()
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and create the current database session """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                                expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ Close the session """
        self.__session.close()
