#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class called square that inherits from the rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        The init method for the class
        Args:
            size: the size of the square, in this case it is
            the width or height.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        return [Square] (<id>) <x>/<y> - <size> -
        in our case, width or height
        """
        a = self.__class__.__name__
        return f"[{a}] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ getting size value """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setting size value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
