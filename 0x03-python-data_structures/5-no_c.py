#!/usr/bin/python3
def no_c(my_string):
        return
    for i in range(len(my_string) - 2):
        if my_string[0] == 'c' or my_string[i] == 'C':
            my_string = my_string[:i] + "" + my_string[i+1:]
    return my_string
