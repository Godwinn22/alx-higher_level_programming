#!/usr/bin/python3
"""Defines a class called Base"""


class Base:
    """
    Defines a class called Base
    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        The class method
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        