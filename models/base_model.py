#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
fmt = '"%Y-%m-%dT%H:%M:%S.%f"'

class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """

    id = Column(String(60), nullable=False, unique=True, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        # if kwargs:
        #     if 'id' not in kwargs:
        #         self.id = str(uuid.uuid4())
        #     if 'created_at' not in kwargs:
        #         self.created_at = datetime.now()
        #     else:
        #         kwargs['created_at'] = datetime.strptime(kwargs["created_at"], fmt)
        #     if 'updated_at' not in kwargs:
        #         self.created_at = datetime.now()
        #     else:
        #         kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], fmt)
        #     for key, val in kwargs.items():
        #         if key != '__class__':
        #             setattr(self, key, val)
        if kwargs:
            for key, value in kwargs.items():
                if (key == "created_at" or key == "updated_at") and key != "__class__":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                if key != "created_at" and key != "updated_at" and key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        try:
            my_dict["created_at"] = self.created_at.isoformat()
        except AttributeError:
            pass
        try:
            my_dict["updated_at"] = self.updated_at.isoformat()
        except AttributeError:
            pass
        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        models.storage.delete(self)
