#!/usr/bin/python3
"""
Module File storage
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    This class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    __file_path = 'file.json'
    __objects = {}
    classes_dict = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                    "Place": Place, "Review": Review, "State": State,
                    "User": User}

    def all(self):
        """Return the dictionary of __object class attributes
        (ex: <class>.<id>)
        """
        return self.__objects

    def new(self, obj):
        """Add new obj to existing __object class attributes"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save serializes __objects to json file (__file_path:file.json)"""
        dic = {}

        for key, obj in self.__objects.items():
            if obj:
                dic[key] = obj.to_dict()
        #  write dict to file
        with open(self.__file_path, 'w') as fd:
            json.dump(dic, fd)

    def reload(self):
        """ deserializes the JSON file to __objects instances
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(self.__file_path, 'r') as fd:
                new_obj = json.load(fd)
            for key, val in new_obj.items():
                class_name = val['__class__']
                class_name = self.classes_dict[class_name]
                self.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass