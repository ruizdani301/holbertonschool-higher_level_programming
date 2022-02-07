#!/usr/bin/python3
"""Created a class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """ class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        print(type(x))
    @property
    def width(self):
        """to retrieve width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set value"""
        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """to retrieve height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """to retrieve value"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        if isinstance(x, int) is not True:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """to retrieve value"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        if isinstance(y, int) is not True:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def display(self):
        """return a rectangle with #"""
        st = ""
        st = '\n' * self.__y

        for i in range(self.__height):
            st = st + " " * self.__x + "#" * self.__width
            if i < (self.__height - 1):
                st = st + '\n'
        print(st)

    def __str__(self):
        """Return string"""
        return "[Rectangle]"+" ("+str(self.id)+")"+" " + str(self.__x) + "/" +\
            str(self.__y)+" - " + str(self.__width)+"/"+str(self.__height)

    def update(self, *args, **kwargs):
        """if args exist set using *args
           if not set attributes with **kwargs
        """
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.__width = v
                elif i == 2:
                    self.__height = v
                elif i == 3:
                    self.__x = v
                else:
                    self.__y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation"""
        dic = {}

        dic["x"] = self.__x
        dic["y"] = self.__y
        dic["id"] = self.id
        dic["height"] = self.__height
        dic["width"] = self.__width
        return dic
