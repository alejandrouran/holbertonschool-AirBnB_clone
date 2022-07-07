#!/usr/bin/python3
"""unittest for review"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):
    """test place class"""

    def setUp(self):
        """test Set method"""
        pass

    def test_place_id_attr(self):
        """test attributes correct types"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id_attr(self):
        """test attributes correct types"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_text_id_attr(self):
        """test attributes correct types"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_str(self):
        """test str method"""
        review = Review()
        string = "[Review]({}){}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))


if __name__ == "__main__":
    unittest.main()
