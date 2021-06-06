#!/usr/bin/python3
"""
Class Rectangle: Defines a Rectangle
"""


class Rectangle:
    """ class that defines a Rectangle with attributes and public methods"""

    def __init__(self, width=0, height=0):
        """ Initialize attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the width of rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width with safe assignement"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the height of rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height with safe assignement"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Return the perimetre of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ magic method that print the rectangle with the character # """
        string = ""
        if (self.__width == 0 or self.__height == 0):
            return (string)
        else:
            for x in range(self.__height):
                for y in range(self.__width):
                    string += '#'
                string += '\n'
            string = string[:-1]
        return (string)

    def __repr__(self):
        """ return a string representation of the rectangle to be
        able to recreate a new instance by using eval()
        """
        wid = str(self.__width)
        hei = str(self.__height)
        return "Rectangle(" + wid + ", " + hei + ")"
