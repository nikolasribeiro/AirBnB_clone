#!/usr/bin/python3


""" Module file_storage"""

import json


class FileStorage:
    """ class FileStorage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ function all """
        return self.__objects

    def new(self, obj):
        """ function new """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ function save """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            """ d = new_dictionary """
            d = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """ function reload """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for key, value in (json.load(file)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
