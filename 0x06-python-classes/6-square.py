#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square():
    """Write a class Square that defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """to retrieve value"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square area"""
        return self.__size ** 2

    def my_print(self):
        """stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            print()
            for j in range(0, self.__size):
                print("{}".format('#'), end="")
        print()
