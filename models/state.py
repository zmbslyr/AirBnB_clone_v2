#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship/
        ('City', cascade='all, delete-orphan', back_populates='state')
    else:
        name = ""

    @property
    def cities(self):
        a_list = []
        attr = models.storage.all(models.city.City).items()
        for key, val in attr.items():
            copy_dict = val.__dict__
            if copy_dict['state_id'] == self.id:
                a_list.append(copy_dict['state_id'])
        return (a_list)
