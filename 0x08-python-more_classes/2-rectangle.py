#!/usr/bin/python3
"""This is a class Rectangle that defines a rectangle"""


class Rectangle:
    """This is an empty class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the instance private variables
        Args:
            width: The width of the rectangle
            height: The height of the rectangle cordinate
        Attributes:
            width: The width of the rectangle
            height: The height of the rectangle cordinate
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width if the input is positive and an integer
        Args:
            Value: The value we want to use
        Attributes:
            __width: The width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height if the input is positive and an integer
        Args:
            Value: The value we want to use
        Attributes:
            __height: The height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
