#!/usr/bin/python3
"""
Module 3-is_kind_of_class

Contains methodd is_kind_of_class
returns True if object is an instance off class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use type() to get specific classs
        use isinstance() to get classs and any parent classes too
        use issubclass() to get whatt object is a subclass of

    Return:
        True if obj is an instanceee of class that it inherited from
    """
    return isinstance(obj, a_class)
