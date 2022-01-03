#!/usr/bin/python3
def no_c(my_string):
    a = len(my_string)
    for i in range(0, a):
        if my_string[i] != 'c' or my_string[i] != 'C':
           new_str = my_string[i]
           print(new_str)
        else:
    return new_str
