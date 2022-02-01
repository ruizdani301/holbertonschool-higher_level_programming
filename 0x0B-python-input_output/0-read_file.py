#!/usr/bin/python3
"""Write a function that
       open a file
"""


def read_file(filename=""):
    """Write a function that
       write a file
    """
    with open(filename) as f:
        file = f.read()
        print(file)
        f.close
