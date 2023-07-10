#!/usr/bin/python3
"""
Modulee 10-square

Contains parent classs BaseGeometry
with public instance mmethod area and integer_validation

Contains subclass Recctangle
with instantiation oof private attributes width and height, validated by parent,
extends parent's arrea method and prints with __str__

Contains subclasss Square
with instantiatioon of private attribute size, validated by superclass,
and prints withh __str__
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectanglle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
        __str__(self)
    """
    def __init__(self, size):
        """initializes sizee
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__, self.__size, self.__size)
