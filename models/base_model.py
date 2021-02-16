#!/usr/bin/python3
""" Module base model """
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ Class Base Model """

    def __init__(self, *args, **kwargs):
        """ Init function constructor """
        if kwargs is not None and kwargs != {}:
            for key in kwargs.keys():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ STR function """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.to_dict())

    def save(self):
        """ Save function """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ ToDict Function """
        alm_diccionario = self.__dict__
        alm_diccionario["__class__"] = type(self).__name__
        alm_diccionario["created_at"] = alm_diccionario["created_at"].isoformat()
        alm_diccionario["updated_at"] = alm_diccionario["updated_at"].isoformat()
        return alm_diccionario
