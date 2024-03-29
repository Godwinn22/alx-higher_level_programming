#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getting width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting width value """
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints to stdout the # character for the rectangle
        by handling x and y
        x is a space
        y is a new line
        """
        for _ in range(self.__y):
            print("")

        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updating the class Rectangle by adding the public method
        def update(self, *args), that assigns an argument to each attribute
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                # self.__dict__.update(kwargs)
                # or
                # self.__dict__[key] = value
                # or
                setattr(self, key, value)
