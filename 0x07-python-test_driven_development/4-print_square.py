#!/usr/bin/python3
"""
This is a function that prints a square with the character #.
It takes one parameter: size
"""


def print_square(size):
    """This is a function that prints a square with the character #.
    Args:
        size: the length of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    print("\n".join(["#" * size] * size))
