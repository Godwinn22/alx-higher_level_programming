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
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.size}" 
