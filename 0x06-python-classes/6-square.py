#!/usr/bin/python3
"""A class that defines a square by"""


class Square:
    """A class that defines a square by"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the instance private variables
        Args:
            size: The size of the square
            position: The position of the square cordinate
        Attributes:
            size: The size of the square
            position: The position of the square cordinate
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

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

    @property
    def position(self):
        """Retrieves the size"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the size if the input is positive and an integer
        Args:
            Value: The value we want to use
        Attributes:
            __size: The size of the square
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
