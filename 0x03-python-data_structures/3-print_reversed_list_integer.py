#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) != 0:
        lo = len(my_list)
        for i in range(lo, 0, -1):
            print("{:d}".format(my_list[i - 1]))
