#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
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
        self.__width = value

    @property
    def height(self):
        """ getting height value """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ setting width value """
        self.__height = value

    @property
    def x(self):
        """ getting x value """
        return self.__x
    
    @x.setter
    def x(self, value):
        """ setting width value """
        self.__x = value

    @property
    def y(self):
        """ getting y value """
        return self.__y
    
    @y.setter
    def y(self, value):
        """setting width value"""
        self.__y = value