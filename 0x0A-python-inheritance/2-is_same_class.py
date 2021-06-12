#!/usr/bin/python3
""" Program that validate that object is exact the same """


def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly an
    instance of the specified class ; otherwise False. """
    return (True if type(obj) is a_class else False)
