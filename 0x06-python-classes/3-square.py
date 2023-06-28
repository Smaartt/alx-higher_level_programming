#!/usr/bin/python3
"""Task_3"""


class Square:
    """This is a class that defines a sqaure"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square"""
        return self.__size ** 2
