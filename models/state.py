#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models

class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan', back_populates='state')

    @property
    def cities(self):
        a_list = []
        attr = models.storage.all(models.city.City).items()        
        for key, val in attr.items():
            copy_dict = val.__dict__
            if copy_dict['state_id'] == self.id:
                a_list.append(copy_dict['state_id'])

        return (a_list)
