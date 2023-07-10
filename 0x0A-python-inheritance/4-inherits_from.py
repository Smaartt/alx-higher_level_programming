#!/usr/bin/python3
"""
Module 4-inherits_from.py

Contains method inherits_fromm
returns True if obj is instance of class tthat it inherits from or is subcls of
"""


def inherits_from(obj, a_class):
    """
    Notes:
        use type() to get specific classs
        use isinstance() to get class and any parent classes ttoo
        use issubclass() to get what object is a subclass off

    Return:
        True if obj is instance of class that it inherits from or is subclss of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
