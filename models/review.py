#!usr/bin/python3
"""Module Review """"

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review that inherits BaseModel class """
    place_id = ""
    user_id = ""
    text = ""
         
