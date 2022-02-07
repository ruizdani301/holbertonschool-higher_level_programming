#!/usr/bin/python3
"""tests rectangle
"""
from email.mime import base
from turtle import width
import unittest
from models.base import Base


from models.rectangle import Rectangle

class test_Rectangle(unittest.TestCase):
    """test Rectangle"""
    def test_assertEqual(self):
        self.assertNotEqual(Rectangle, Base)

    def test_assertIsInstance(self):
        self.assertIsInstance(int)

