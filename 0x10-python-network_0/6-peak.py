#!/usr/bin/python3
""" peak function"""


def find_peak(list_of_integers):
    """find_peak"""
    arr = len(list_of_integers)
    list = list_of_integers
    if len(list_of_integers) == 0:
        return (None)
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mitad = int(arr / 2)
    peak = list[mitad]
    if peak > list[mitad - 1] and peak > list[mitad + 1]:
        return peak
    elif peak < list[mitad - 1]:
        return find_peak(list[:mitad])
    else:
        return find_peak(list[mitad + 1:])
