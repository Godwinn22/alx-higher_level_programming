#!/usr/bin/python3
"""defines a class called BaseGeometry."""


class BaseGeometry:
    """This is class called BaseGeometry."""
    def area(self):
        """A function that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Another method that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
