#!/usr/bin/python3
def no_c(my_string):
    traslation = my_string.maketrans({ord('C'): None, ord('c'): None})
    new_str = my_string.translate(traslation)
    return new_str
