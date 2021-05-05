#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        if len_a == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if len_b < 2:
        if tuple_b == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    tuple_c = (a, b)
    return tuple_c
