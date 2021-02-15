#!/usr/bin/python3
""" Module base model """
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Class Base Model """
    def __init__(self):
        """ Init function constructor """
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ STR function """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.to_dict())

    def save(self):
        """ Save function """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ ToDict Function """
        alm_diccionario = self.__dict__
        alm_diccionario["__class__"] = type(self).__name__
        alm_diccionario["created_at"] = alm_diccionario["created_at"].\
            isoformat()
        alm_diccionario["updated_at"] = alm_diccionario["updated_at"].\
            isoformat()
        return alm_diccionario
