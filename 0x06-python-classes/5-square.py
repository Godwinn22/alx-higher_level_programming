#!/usr/bin/python3
"""a class Square that defines a square by:
Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it
"""


class Square:
    """A class representing a square."""
    def __init__(self, size=0):
        """Initializes the instance private variables
        Args:
            size: The size of the square
        Attributes:
            size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size  # we protect our data using __

    @size.setter
    def size(self, value):
        """Sets the size if the input is positive and an integer
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
        """Returns the current square area"""
        return self.size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print("")
        for _ in range(self.size):
            print("#" * self.size)
