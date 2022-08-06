#!/usr/bin/python3

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """ Testing FileSorage"""

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

    def test_all(self):
        storage = FileStorage()
        all_dic = storage.all()
        self.assertIsNotNone(all_dic)
        self.assertEqual(type(all_dict), dict)
        self.assertIs(all_dic, storage._FileStorage__objects)

    def test_new(self):
        new_storage = FileStorage()
        all_dic = new_storage.all()
        Mulu = User()
        Mulu.id = 114089
        Mulu.name = "Mulubrhan"
        new_storage.new(Mulu)
        key = Mulu.__class__.__name__ + "." + str(Mulu.id)
        self.assertIsNotNone(all_dic[key])

    def test_reload(self):
        add_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as fw:
            fw.write("{}")
        with open("file.json", "r") as fr:
            for line in fr:
                self.assertEqual(line, "{}")
        self.assertIS(add_storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
