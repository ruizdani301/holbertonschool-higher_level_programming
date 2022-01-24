#!/usr/bin/python3
"""
     Area and Perimeter
     Write a class Rectangle that defines a rectangle
     by: (based on 1-rectangle.py)
"""


class Rectangle:
    """
    define Rectangle
    this module define rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            to retrieve width
            that defines a rectangle by: (based on 7-rectangle.py)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter width
            that defines a rectangle by: (based on 7-rectangle.py)
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("with the message width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            to retrieve height
            that defines a rectangle by: (based on 7-rectangle.py)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter height
            that defines a rectangle by: (based on 7-rectangle.py)
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height the message width must be >= 0")
        self.__height = value

    def area(self):
        """
            Return area
            that defines a rectangle by: (based on 7-rectangle.py)
        """
        return self.width * self.height

    def perimeter(self):
        """
            return perimeter
            that defines a rectangle by: (based on 7-rectangle.py)
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
            print character #
            that defines a rectangle by: (based on 7-rectangle.py)
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        strc = ''
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                strc += str(self.print_symbol)
            strc += '\n'
        return strc[0:-1]

    def __repr__(self):
        """ Write a class Rectangle
            that defines a rectangle by: (based on 7-rectangle.py)
        """
        return "Rectangle({}, {})".format(self.__height, self.__width)

    def __del__(self):
        """
            delete a instance
            that defines a rectangle by: (based on 7-rectangle.py)
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Write a class Rectangle that defines a
            rectangle by: (based on 7-rectangle.py)
        """
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
