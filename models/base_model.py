#!/usr/bin/python3

""" Model BaseModel Parent of all classes"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """Intialize the attributes:
        random uuid, date create or  update"""
        if kwargs:
            for key, value in kwargs.item():
                if "created_at" == key:
                    self.created_at = datetime.strptime(
                            kwargs["created_at"],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(
                            kwargs["update_at"],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    # for the we are not doing anything with class
                    pass
                else:
                    setattr(self, key, value)
        else:
            # Generate a random uuid
            self.id = str(uuid.uuid4())
            # assign current date time when an instance is created
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # If It's new instance add to the models
            models.storage.new(self)

    def __str__(self):
        """returns ifo about model in string format"""
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """returns string represantation"""
        return (self.__str__())

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""

        self.updated_at = datetime.now()
        models.storage.sasve()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance:
        """

        # define dictionary that adds class name as element
        dic = {}
        dic["__class__"] = type(self).__name__
        # loop over the dict items, and convert create_at and update_at to ISO format
        for key, val in self.__dict__.items():
            if isinstance(val, (datetime, )):
                dic[key] = val.isoformat()
            else:
                dic[key] = val
        return dic
