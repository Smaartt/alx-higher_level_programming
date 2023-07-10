#!/usr/bin/python3
"""
Modulee 8-rectangle

Contains parent class BaseGeommetry
with public instance method aarea and integer_validator

Contains subclass Rectanglee
with instantiation of private atttributes width and height, validated by parent
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeomettry
    Methods:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """validate and initiaalize width and height
        Args:
            width (int): private
            height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
