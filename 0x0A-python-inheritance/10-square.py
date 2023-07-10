#!/usr/bin/python3
"""
Modulee 10-square

Contains parent class BaseGeommetry
with public instance method aarea and integer_validation

Contains subclass Rectanglee
with instantiation of privaate attributes width and height, validated by parent,
extends parent's area methhod and prints with __str__

Contains subclass Squaree
with instantiation of privatte attribute size, validated by superclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectanngle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """initializes sizze
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
