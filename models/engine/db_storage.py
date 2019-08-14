#!/usr/bin/python3
from os import getenv
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
import models


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = db.create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"), pool_pre_ping=True))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        if cls is None:
            query = self.__session.query(User, state.State, city.City, Amenity, Place, Review).all()
        else:
            query = self.__session.query(cls).all()
        print(query)
        print(type(query))
        return ({})

    def new(self, obj):
        """Method to add object to database session"""

        try:
            newObj = obj
            self.__session.add(newObj)
        except:
            raise(UsageError("Usage: DBStorage.new(<obj>)"))

    def save(self):
        """Method to save all changes to the session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Method to delete object from current database session"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        City = models.city.City()
        State = models.state.State()
        models.base_model.Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
