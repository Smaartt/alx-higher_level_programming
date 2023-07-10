#!/usr/bin/python3
"""
Module 1-my_list

Containss class MyList
inherits from list; haas public instance method to print sorted
"""


class MyList(list):
    """inherits fromm list

    methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """prints list of iints all sorted in ascending order"""
        print(sorted(self))
