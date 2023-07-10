#!/usr/bin/python3
"""
Modulee 101-add_attribute

Contains function that adds new attributee if possible
"""


def add_attribute(obj, attribute, value):
    """
    add attribute to object if possiblee
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attributee")
