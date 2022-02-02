#!/usr/bin/python3
"""Write a function that returns the dictionary description
   with simple data structure
"""
import json


def class_to_json(obj):
    """Write a function that returns the dictionary description
       with simple data structure
    """
    return json.dumps(obj, default=lambda obj: obj.__dict__)
