#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    x, y = 0, 0
    for (i, j) in my_list:
        x += (i * j)
        y += i
    return x / y
