#!/usr/bin/python3
"""Write a function that writes an Object to a text file,
   using a JSON representation:
"""
import json

def save_to_json_file(my_obj, filename):
    """Write a function that writes an Object to a text file,
       using a JSON representation:
    """
    txt = json.dumps(my_obj)
    with open(filename, 'w') as f:
        w_file = f.write(txt)
        f.close
        #return w_file
