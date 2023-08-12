#!/usr/bin/env python3
"""
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''class for TestReview'''
    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()