#!/usr/bin/python3
"""define a function to verify the instance of an object"""


def is_same_class(obj, a_class):
    """This is a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return (True)
    return (False)
