#!/usr/bin/python3
"""Defines a function that adds a new attribute
to an object if it’s possible
"""


def add_attribute(obj, att, value):
    """ A function that adds a new attribute to an object if it’s possible.
    Args:
        obj(any): the object to add an attribute to
        att(str): the name of the attribute to add
        value(any): the value of attribute
    Raises:
        TypeError: if the attribute can not be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att, value)
