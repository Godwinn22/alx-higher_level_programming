#!/usr/bin/python3
"""This is a class Rectangle that defines a rectangle"""


class Rectangle:
    """
    This is an empty class Rectangle that defines a rectangle
    Attributes:
        number_of_instances: the number of instances
    """
    number_of_instances = 0
    print_symbol = "#"

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
        self.__class__.number_of_instances += 1

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

    def __str__(self):
        """Returns the string representation of an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol)
                          * self.__width] * self.__height)

    def __repr__(self):
        """Returns the string representation of an object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """This method is called when a deletion happens"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This is a static method that returns the biggest rectangle
        based on the area.
        Args:
            rect_1: the first rectangle
            rect_2: the second rectangle
        Attributes:
            area1: the first rectangle area
            area2: the second rectangle area
        """
        area1 = rect_1.area()
        area2 = rect_2.area()
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if area1 == area2:
            return rect_1
        elif area2 > area1:
            return rect_2
        else:
            return rect_1
