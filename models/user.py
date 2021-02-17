#!/usr/bin/python3


""" Module models/user"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
