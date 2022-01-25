#!/usr/bin/python3
"""
    Module say my name
    Write a function that prints a
    square with the character #.
"""


def say_my_name(first_name, last_name=""):
    """
        print the first name and last name
        Prototype: def print_square(size):
        size is the size length of the square
        size must be an integer, otherwise raise a
        TypeError exception with the message size must
        be an integer.
    """

    if type(first_name) is not (str):
        raise TypeError("first_name must be a string")
    if type(last_name) is not (str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
