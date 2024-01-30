#!/usr/bin/python3
"""This is a class Square that defines a square by with
Private instance attribute: size
"""


class Square:
    """This is a class Square that defines a square"""
    def __init__(self, size=0):
        """This is the init method use to initialise the object attr
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

    def area(self):
        """This is a method that calculates the area of a square
        Returns:
            int: the area of the square
        """
        return self.__size ** 2
