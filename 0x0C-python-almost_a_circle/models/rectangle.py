#!/usr/bin/python3
""" First Rectangle that inherits from Base """


class Rectangle(Base):
    """ class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Retriebe the width of rectangle """
        return(self.__width)

    @width.setter
    """ set passet private attribute of width """

    def width(self, value):
        self.__width = value
