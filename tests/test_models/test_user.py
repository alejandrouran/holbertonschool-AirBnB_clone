#!/usr/bin/python3
"""unittest for state"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    """test User class"""

    def setUp(self):
        """test Set method"""
        pass

    def test_first_name_attr(self):
        """test attributes correct types"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_str(self):
        """test str method"""
        user = User()
        string = "[User]({}){}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))


if __name__ == "__main__":
    unittest.main()
