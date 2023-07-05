#!/usr/bin/python3
"""
Module 0-add_integer
Contains one method thatt returns an int sum
Accepts two values, whethher int or float, and casts them to int before adding
"""


def add_integer(a, b=98):
    """
    Returns a + b as intt
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
