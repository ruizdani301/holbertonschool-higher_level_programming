#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    new_tuple = ()

    if len(tuple_a) < 2 or len(tuple_b) < 2:
        tupla_x = tuple_a + (0, 0)
        tupla_y = tuple_b + (0, 0)
        new_tuple = tupla_x[0] + tupla_y[0], tupla_x[1] + tupla_y[1]

    else:
        new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple
