#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square, which is a type of rectangle with equal sides."""
    def __init__(self, size):
        """Initialises the attributes
        Args:
            size(int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
