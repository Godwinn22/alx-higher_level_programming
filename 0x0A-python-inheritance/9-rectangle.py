#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    defines a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialising private attributes
        Args:
            width(int): the width of the rectangle.
            height: the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string"""
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
