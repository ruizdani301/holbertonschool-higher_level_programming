#!/usr/bin/python3
"""
    function that prints a square with the character #.
"""


def print_square(size):
    """
        print square with the character #
    """

    # se quita !=True
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for m in range(0, size):
            print("{}".format("#"), end="")
        print()
