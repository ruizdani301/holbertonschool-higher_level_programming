#!/usr/bin/python3
"""an instance of the specified class;
   otherwise False
"""


def is_same_class(obj, a_class):
    """
       this function return
       True if the object is exactly
       an instance of the specified class ; otherwise False
    """
    if (type(obj) is a_class):
        return (True)
    else:
        return (False)
