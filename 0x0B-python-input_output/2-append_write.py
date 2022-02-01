#!/usr/bin/python3
"""Write a function that appends a string
   at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """Write a function that appends a string
       at the end of a text file (UTF8)
    """
    with open(filename, 'a') as f:
        w_file = f.write(text)
        f.close
        return w_file
