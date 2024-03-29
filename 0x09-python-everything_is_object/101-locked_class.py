#!/usr/bin/python3
"""Defines a class LockedClass with no class or object attribute"""


class LockedClass:
    """a class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name
    Args:
        __slots__: for setting slots
    """
    __slots__ = ["first_name"]
