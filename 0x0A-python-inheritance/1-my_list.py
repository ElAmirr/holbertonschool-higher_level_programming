#!/usr/bin/python3
"""
Program that print a sorted list 
"""


class MyList(list):
    """ Class that inherit from list """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """

        self.sort()
        print(self)
