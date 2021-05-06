#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string:
        for elm in my_string:
            if elm != 'c' or elm != 'C':
                new_string += elm
        return new_string
    return
