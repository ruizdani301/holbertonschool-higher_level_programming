#!/usr/bin/python3
"""
    Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py).

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class
        """

    def __init__(self, size):
        """init function
        """

        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        """ Return area
            defines a rectangle by: (based on 4-rectangle.py)
        """
        return self.__size**2
