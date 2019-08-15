#!/usr/bin/python3
"""This is the user class"""
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


class User(models.base_model.BaseModel,
           models.base_model.Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
#        places = relationship("Place", back_populates="user")
#        reviews = relationship("Review", back_populates="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
