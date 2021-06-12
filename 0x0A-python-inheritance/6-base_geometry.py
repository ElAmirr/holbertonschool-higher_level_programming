#!/usr/bin/python3
""" Empty Geometry Class """


class BaseGeometry:
    """ raises an Exception with the message area() is not implemented """

    def area(self):
        raise Exception("area() is not implemented")
