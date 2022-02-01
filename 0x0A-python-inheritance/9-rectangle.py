#!/usr/bin/python3
"""
    Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py).

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
            init instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ Return area
            defines a rectangle by: (based on 4-rectangle.py)
        """
        return self.__width * self.__height

    def __str__(self):
        """ rectangle description:
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
