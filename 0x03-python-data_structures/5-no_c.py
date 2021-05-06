#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new_string = ""
    length = len(new_string)
    for elm in range(length):
        if my_string[elm] != 'c' and my_string[elm] != 'C':
            new_string += my_string[elm]
    return new_string
