#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new_string = ""
    for elm in my_string:
        if elm != 'c' or elm != 'C':
            new_string += elm
    return new_string
