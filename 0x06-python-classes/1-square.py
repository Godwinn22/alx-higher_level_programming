#!/usr/bin/python3
"""a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""


class Square:
    """This a class Square that defines a square by: (based on 0-square.py)"""
    def __init__(self, size):
        """ This a class Square that defines a square by:(based on 0-square.py)
        Args:
            size: the size of a square.
        """
        self.__size = size
