#!/usr/bin/python3
"""This is a class Square that defines a square by
Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it
"""


class Square:
    """This is a class Square that defines a square by"""
    def __init__(self, size=0):
        self.size = size
        
    @property  # getter method for 'size' property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size
    
    @size.setter  # setter method for 'size' property
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size ** 2
    