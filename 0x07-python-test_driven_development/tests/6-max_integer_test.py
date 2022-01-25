#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class text_integer(unittest.TestCase):
    """ class max integer """


    def test_regular(self):
        """regular test with list of ints"""
        l = [2, 4, 6, 8, 10]
        result = max_integer(l)
        self.assertEqual(result, 10)

    def test_non_int(self):
        """non integers Test:
        raise a TypeError exception"""
        l = ["x", "y", 10]
        self.assertRaises(TypeError, max_integer, l)

    def variable_undefine(self):
        """variable undefined"""
        l = [x]
        self.assertRaises(NameError, defined, l)

    def test_empty(self):
        """ parameter None"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def compare(self):
        """ campare type """
        l = [1, 2]
        self.assertIsInstance(l, list)

if __name__ == "__main__":
    unittest.main()
