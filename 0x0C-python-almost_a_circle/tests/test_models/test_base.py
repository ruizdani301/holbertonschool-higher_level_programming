#!/usr/bin/python3
"""tests base
"""
import unittest

from models.base import Base

class test_Base(unittest.TestCase):
    """ class base """
    def test_isinstancia(self):
        b_1 = Base()
        self.assertIsInstance(b_1, Base)

    def test_equal(self):
        c_1 = Base()
        self.assertEqual(c_1.id, 1)
        c_2 = Base()
        self.assertEqual(c_2.id, 2)

    def test_noequal(self):
        c_1 = Base()
        self.assertNotEqual(c_1, 2)
        c_2 = Base()
        self.assertNotEqual(c_2.id, 1)

