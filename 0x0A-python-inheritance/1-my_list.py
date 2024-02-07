#!/usr/bin/python3
"""This is a class MyList that inherits from list
"""


class MyList(list):
    """This is a class MyList that inherits from list.
    """

    def print_sorted(self):
        """This is a function that prints a sorted list"""
        print(sorted(self))
