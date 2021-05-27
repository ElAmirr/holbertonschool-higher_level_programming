#!/usr/bin/python3
def weight_average(my_list=[]):
    x, y = 0, 0
    if my_list:
        for i, j in my_list:
            x += (i * j)
            y += i
        return x // y
    else:
        return 0
