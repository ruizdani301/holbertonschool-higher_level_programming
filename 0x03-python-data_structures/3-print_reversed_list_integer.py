#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = 1
    lo = len(my_list)
    while(a != lo + 1):
        print("{:d}".format(my_list[- (a)]))
        a = a + 1
