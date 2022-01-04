#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return "None"
    new = my_list[:]
    o = sorted(new)
    return o.pop()
