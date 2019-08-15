#!/usr/bin/python3
"""This is the user class"""
# from models.base_model import BaseModel
import models

class User(models.base_model.BaseModel):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
