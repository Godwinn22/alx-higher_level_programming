#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square, which is a type of rectangle with equal sides.
    Initialises the attributes
    Args:
        size(int): the size of the square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """Returns the area of this square."""
        return self.__size ** 2
    
    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__, self.__size, self.__size)