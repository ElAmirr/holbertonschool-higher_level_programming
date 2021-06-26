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

    @property
    def height(self):
        """ Retrieb the height of rectangle """
        return(self.__height)

    @height.setter
    """ set passet private attribute of height """

    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ Retrieve private instance attribute x """
        return(self.__x)

    @x.setter
    def x(self, value):
        """ set passet private instance attribute x"""
        self.__x = value

    @property
    def y(self):
        """ Retrieve private instance attribute y"""
        return(self.__y)

    @y.setter
    def y(self, value):
        """ set passet private instance attribute y"""
        self.__y = Value
