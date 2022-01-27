#!/usr/bin/python3
"""
The ``test_base_model`` module
==============================

Using ``test_base_model``
-------------------------

This is a test_base_model unittest file to test the base_model module.

"""
import unittest
from models.base_model import BaseModel
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """Defines a class TestBaseModel.

    Test functionality of the base_model module.
    """
    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_create(self):
        """Test if the created class is same type."""
        a = BaseModel()
        self.assertIsInstance(a, BaseModel)

    def test_id(self):
        """Tests if id is of type str."""
        a = BaseModel()
        self.assertEqual(type(a.id), str)

    def test_time(self):
        """Tests if the created and updated date is equal at creation."""
        a = BaseModel()
        self.assertEquals(a.created_at, a.updated_at)

    def test_created_at(self):
        """Tests if created_at is of type datetime."""
        a = BaseModel()
        self.assertEqual(type(a.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test is updated_at is of type datetime."""
        a = BaseModel()
        self.assertEqual(type(a.updated_at), datetime.datetime)

    def test_str(self):
        """Tests if the string representation is correct format."""
        obj = BaseModel()
        self.assertEqual(str(obj), '[{}] ({}) {}'.format("BaseModel", obj.id,
                         obj.__dict__))

    def test_save(self):
        """Tests if the saved attributes are the same as the original."""
        obj = BaseModel()
        obj.save()
        key = "BaseModel" + "." + obj.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], obj.to_dict())
