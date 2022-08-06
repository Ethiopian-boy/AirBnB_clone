#!/usr/bin/python3

import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.city1 = City()
        cls.city1.name = "Rajkot"
        cls.city1.state_id = "IN"

    @classmethod
    def tearDown(cls):
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_checking_fnctions(self):
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)

    def test_attribute_are_str(self):
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

    def test_save(self):
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)
    
    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.city1), True)


if __name__ == "__main__":
    unittest.main()
