#!/usr/bin/python3
from os import getenv
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class DBStorage:

    __engine = None
    __session = None
    __session_factory = None

    def __init__(self):
        self.__engine = db.create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True))

        if getenv('HBNB_ENV') == 'test':
            models.base_model.Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        a_dict = {}
        if cls is None:
            query = self.__session.query(User,
                                         State,
                                         City,
                                         Amenity,
                                         Place,
                                         Review).all()
        else:
            query = self.__session.query(cls).all()
        for obj in query:
            key = obj.__class__.__name__ + str(obj.id)
            a_dict.update({key: obj})
        return (a_dict)

    def new(self, obj):
        """Method to add object to database session"""

        self.__session.add(obj)

    def save(self):
        """Method to save all changes to the session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Method to delete object from current database session"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload mySQL tables"""
        models.base_model.Base.metadata.create_all(self.__engine)
        if self.__session_factory is None:
            self.__session_factory = scoped_session(
                sessionmaker(bind=self.__engine)
            )
        if self.__session is not None:
            self.__session.close()
        self.__session = self.__session_factory(expire_on_commit=False)
