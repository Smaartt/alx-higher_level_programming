#!/usr/bin/python3
"""
Module 2-is_same_classs

Contains method is_same_classs
returns True if object is exactly ann instance of specified class
"""


def is_same_class(obj, a_class):
    """
    Notes:
        use type() to get specificc class
        use isinstance() to gett class and any parent classes too
        use issubclass() to gett what object is a subclass of

    Return:
        True if obj is exactlyy an instance of specified class
    """
    return type(obj) == a_class
