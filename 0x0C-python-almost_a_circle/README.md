# This is a readme file for my ALX project "0x0C-python -almost-a-circle."#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    def __ init__(self, width, height, x=0, y=0, id=None):
        super().__ init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        """ getting width value """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ setting width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getting height value """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ setting height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getting x value """
        return self.__x
    
    @x.setter
    def x(self, value):
        """ setting x value """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getting y value """
        return self.__y
    
    @y.setter
    def y(self, value):
        """ setting y value """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value