#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        else:
            new[i] = new[:i] + "" + char
            i = i + 1
        return new
