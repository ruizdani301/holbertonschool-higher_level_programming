#!/usr/bin/python3
"""
    Real definition of a rectangle
    Write a class Rectangle that defines a rectangle
    by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
        define Rectangle.
        this module define rectangle
    """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
            to retrieve width
            defines a rectangle by: (based on 1-rectangle.py)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter width
            defines a rectangle by: (based on 1-rectangle.py)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            to retrieve height
            defines a rectangle by: (based on 0-rectangle.py)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter height
            defines a rectangle by: (based on 1-rectangle.py)
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
