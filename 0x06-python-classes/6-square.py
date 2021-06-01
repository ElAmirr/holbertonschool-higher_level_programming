#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        s = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(s)
        elif (len(value) != 2):
            raise TypeError(s)
        else:
            for t in value:
                if (t < 0):
                    raise TypeError(s)
                elif (type(t) is not int):
                    raise TypeError(s)
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.size != 0):
            for n in range(self.__position[1]):
                print("")
            for x in range(self.__size):
                for y in range(self.__size + self.__position[0]):
                    if (y < self.__position[0]):
                        print(" ", end='')
                    else:
                        print("#", end='')
                print('')
        else:
            print('')
