#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) != None:
        lo = len(my_list)
        for i in range(lo, 0, -1):
            print("{:d}".format(my_list[i - 1]))
