#!/usr/bin/python3
"""Task_4"""


class Square:
    """This is a clas that defines a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter for the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return only the current square"""
        return self.__size ** 2
