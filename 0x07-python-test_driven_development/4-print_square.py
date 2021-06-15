#!/usr/bin/python3
"""
Progam that print square with # symbol according to input size
"""


def print_square(size):
    """ function that prints a square with the character # """
    if not(isinstance(size, int)):
        raise TypeError('size must be an integer')
    if (size < 0):
        raise ValueError('size must be >= 0')
    if (isinstance(size, float) and size < 0):
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print('')
