#!/usr/bin/python3
"""unittest for place"""
import unittest
from models.base_model import BaseModel
from models.place import place
from models.engine.file_storage import FileStorage
import os


class testPlace(unittest.TestCase):
    """test place class"""

    def setUp(self):
        """test Set method"""
        pass

    def test_attr(self):
        """test attributes correct types"""
        city = Place()
        self.assertTrue(hasttr(place, "name"))
        self.assertEqual(place.name, "")

    def test_str(self):
        """test str method"""
        place = Place()
        string = "[Place]({}){}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))


if __name__ == "__main__":
    unittest.main()
