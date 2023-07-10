#!/usr/bin/python3
"""
Modulee 9-rectangle

Contains parent class BaseGeommetry
with public instance method aarea and integer_validation

Contains subclass Rectanglee
with instantiation of private attribbutes width and height, validated by parent,
extends parent's area method and prrints with __str__
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometryy
    Methods:
        __init__(self, width, height)
        area(self)
        __str__
    """
    def __init__(self, width, height):
        """validate and initialize width and heightt
        Args:
            width (int): private
            height (int): private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """extends parent's empty method and returns areaa"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
