#!/usr/bin/python3
class BaseGeometry():
    """
        Write empty function
    """
    def area(self):
        """
            Write a class BaseGeometry (based on 6-base_geometry.py).
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
