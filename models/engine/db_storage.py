#!/usr/bin/python3
from os import getenv
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.base_model import BaseModel, Base

class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = db.create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"), pool_pre_ping=True))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        a_dict = {}
#        list_of_classes = [User, State, City, Amenity, Place, Review]
        list_of_classes = [State, City, User, Place, Review]
        if cls is not None:
            query = self.__session.query(cls).all()
            for obj in query:
                dict_of_obj = obj.to_dict()
                key = dict_of_obj['__class__'] + '.' + dict_of_obj['id']
                a_dict[key] = obj
        elif cls is None:
            for classes in list_of_classes:
                query = self.__session.query(classes).all()
                for obj in query:
                    dict_of_obj = obj.to_dict()
                    key = dict_of_obj['__class__'] + '.' + dict_of_obj['id']
                    a_dict[key] = obj
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
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
