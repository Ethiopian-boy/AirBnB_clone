#!/usr/bin/python3

import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.review1 = Review()
        cls.review1.place_id = "Ok"
        cls.review1.user_id = "Muller"
        cls.review1.text = "Welcome!"

    @classmethod
    def tearDown(cls):
        del cls.review1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.review1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.review1.__dict__)
        self.assertTrue('created_at' in self.review1.__dict__)
        self.assertTrue('Updated_at' in self.review1.__dict__)
        self.assertTrue('user_id' in self.review1.__dict__)
        self.assertTrue('place_id' in self.review1.__dict__)
        self.assertTrue('text' in self.review1.__dict__)

    def test_attributes_are_str(self):
        self.assertEqual(type(self.review1.place_id), str)
        self.assertEqual(type(self.review1.text), str)

    def test_save(self):
        self.review1.save()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to dict' in dir(self.review1), True)


if __name__ == "__main__":
    unittest.main()
