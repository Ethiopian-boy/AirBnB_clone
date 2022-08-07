#!/usr/bin/python3
"""
Unit test for BaseModel Class
"""
from datetime import datetime
from time import time
import unittest
import models


BaseModel = models.base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_instantiation(self):
        """Testing if object is correctly created"""
        instance = BaseModel()
        self.assertIs(type(instance), BaseModel)
        instance.name = "My First Model"
        instance.number = 89
        attri_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attri, ty in attri_types.items():
            with self.subTest(attri=attri, ty=ty):
                self.assertIn(attri, instance.__dict__)
                self.assertIs(type(instance.__dict__[attri]), ty)
        self.assertEqual(instance.name, "My First Model")
        self.assertEqual(instance.number, 89)

    def test_datetime_attr(self):
        """Test BaseModel instances have similar
        updated_at and created_at at creation
        and different updated_at after save(update).
        """
        obj = BaseModel()
        self.assertTrue(obj.created_at, obj.updated_at)
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        for inst in [instance1, instance2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(
                        uuid,
                        '^[0-9a-f]{8}-[0-9a-f]{4}'
                        '-[0-9a-f]{4}-[0-9a-f]{4}'
                        '-[0-9a-f]{12}$')
        self.assertNotEqual(instance1.id, instance2.id)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "BaseModel"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected = ["id",
                    "created_at",
                    "updated_at",
                    "name",
                    "my_number",
                    "__class__"]
        self.assertCountEqual(d.keys(), expected)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "BaseModel")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """Tests that values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        base_model = BaseModel()
        new_d = base_model.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(
                new_d["created_at"],
                base_model.created_at.strftime(time_format))
        self.assertEqual(
                new_d["updated_at"],
                base_model.updated_at.strftime(time_format))

    def test_str(self):
        """Test that the str methof has correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))


if __name__ == "__main__":
    unittest.main()
