#!/usr/bin/python3
"""This is a class Square that defines a square by
Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it
"""


class Square:
    """This is a class Square that defines a square by"""
    def __init__(self, size=0):
        """Initializes the instance private variables
        Args:
            size: The size of the square
        Attributes:
            size: The size of the square
        """
        self.size = size

    @property  # getter method for 'size' property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter  # setter method for 'size' property
    def size(self, value):
        """This instance is used to set the property
        Args:
            Value: The value we want to use
        Attributes:
            __size: The size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size ** 2
