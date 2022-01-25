#!/usr/bin/python3
"""
    Module add integer a + b
"""


def add_integer(a, b=98):
    """
        Function add a + b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    c = a + b
    # se quito == True
    if isinstance(c, float):
        c = int(c)

    return c
