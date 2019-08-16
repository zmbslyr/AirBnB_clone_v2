#!/usr/bin/python3
"""This is the amenity class"""
# from models.base_model import BaseModel
import models


class Amenity(models.base_model.BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    name = ""
