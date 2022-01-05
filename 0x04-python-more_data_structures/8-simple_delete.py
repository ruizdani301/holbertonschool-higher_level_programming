#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    x = a_dictionary.get(key)
    if x != 0:
        del a_dictionary[key]
        return a_dictionary
    #return a_dictionary

        