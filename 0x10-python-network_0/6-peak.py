#!/usr/bin/python3
""" peak function"""


def find_peak(list_of_integers):
    """find_peak"""
    arr = list_of_integers
    if len(list_of_integers) == 0:
        return (None)
    else:
        inicio = 1
        final = len(list_of_integers) - 1
        peak = set()
        for i in range(inicio, final):
            izq = i - 1
            der = i + 1
            if arr[izq] <= arr[i] and arr[der] <= arr[i]:
                peak.add(list_of_integers[i])
        peak = list(peak)
        return(peak)
