#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:]
    new_list[idx1] = element
    return new_list