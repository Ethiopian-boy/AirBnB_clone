#!/usr/bin/python3
"""Modele place class """

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Inherits from BaseModel
    public class attribute:
    city_id:            (str) it will be the City.id
    user_id:            (str) it will be the User.id
    name:               (str)
    description:        (str)
    number_rooms:       (int) 0
    number_bathrooms:   (int) 0
    max_guest:          (init) 0
    price_by_night:     (int) 0
    latitude:           (float) 0
    longitude:          (float) 0
    amenity_ids:        (list) it will be the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
