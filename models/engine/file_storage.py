#!/usr/bin/python3

""""
File storage
Convert the dictionary representation to JSON string
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import state
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os.path import isfile


class FileStorage:
    """a class that serializes instances to a JSON file and deserializes
    JSON file to instances:"""

    __file_path  = "file.json"
    __objects = {}
    class_dict = {"BaseMode": BaseModel, "User": user, "place": Place,
            "Amenity": Amenity, "City": City, "Review": Review,
            "State": State}

    def all(self):
        """Returns the dictionary of __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}
        with open(self.__file_path, 'w') as f:
            for val in self.__objects.values():
                key = '{}.{}'.format(val.__class__.__name__, val.id)
                my_dict[key] = val.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        # check if file exists
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)
            for key, val in json_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
