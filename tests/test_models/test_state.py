"""unittest for review"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):
    """test place class"""

    def setUp(self):
        """test Set method"""
        pass

    def test_name_attr(self):
        """test attributes correct types"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_str(self):
        """test str method"""
        state = State()
        string = "[State]({}){}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))


if __name__ == "__main__":
    unittest.main()