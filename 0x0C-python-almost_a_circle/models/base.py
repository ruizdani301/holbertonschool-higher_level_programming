#!/usr/bin/python3
"""Module Initialization
"""
import json


class Base:
    """Module Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
        """
        if id is None:
            Base.__nb_objects = self.__nb_objects + 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
           of list_dictionaries
           If list_dictionaries is None or empty,
           return the string: "[]
        """
        ld = list_dictionaries
        if ld is None or len(ld) == 0:
            return "[]"
        return json.dumps(ld)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
           of list_objs to a file:
        """
        ls = []
        if list_objs is not None:
            for i in list_objs:
                ls.append(cls.to_dictionary(i))
            file = cls.__name__ + ".json"
            with open(file, "w+") as f:
                f.write(cls.to_json_string(ls))
