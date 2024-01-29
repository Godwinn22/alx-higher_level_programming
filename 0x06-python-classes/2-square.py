#!/usr/bin/python3
"""This is a class that defines a square by"""


class Square:
    """This is a class that defines a square by"""
    def __init__(self, size=0):
        """This is the init function that is used
        to initialise the object's attributes
        Args:
            size: the size of the square

        Attributes:
            __size: the private instance attributes
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
