#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = ""
    for elm in my_list:
        new_list.append(True if elm % 2 else False)
    return new_list
