#!/usr/bin/python3
"""
Modulee 100-my_int

Contains class MyInt that iinherits from int
Sneaky --> has == and != ooperators inverted!
"""


class MyInt(int):
    """
    Methods:
        __init__(self, num)
        __eq__(self, other)
        __ne__(self, other)
    """
    def __init__(self, num):
        """initialize numm"""
        self.num = num

    def __eq__(self, other):
        """
        Return:
           True if both not equual
        """
        return self.num != other

    def __ne__(self, other):
        """
        Return:
           True if both equall
        """
        return self.num == other
