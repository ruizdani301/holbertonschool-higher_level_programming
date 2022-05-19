#!/usr/bin/python3
""" peak function"""


def find_peak(list_of_integers):
    """find_peak"""
    arr = len(list_of_integers)
    if len(list_of_integers) == 0:
        return (None)
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mitad = int(arr / 2)
    peak = list_of_integers[mitad]
    if peak > list_of_integers[mitad - 1] and peak > list_of_integers[mitad + 1]:
        return peak
    elif peak < list_of_integers[mitad - 1]:
        return find_peak(list_of_integers[:mitad])
    else:
        return find_peak(list_of_integers[mitad + 1:])
