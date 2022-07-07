#!/usr/bin/python3
"""unittest for place"""
import unittest
from models.base_model import BaseModel
from models import place
from models.engine.file_storage import FileStorage
import os
Place = place.Place


class TestPlace(unittest.TestCase):
    """test place class"""

    def setUp(self):
        """test Set method"""
        pass

    def test_city_id_attr(self):
        """test attributes correct types"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """test attributes correct types"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_name_attr(self):
        """test attributes correct types"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_str(self):
        """test str method"""
        place = Place()
        string = "[Place]({}){}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))


if __name__ == "__main__":
    unittest.main()
