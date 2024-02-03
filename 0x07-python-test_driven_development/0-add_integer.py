#!/usr/bin/python3
"""
This a function that adds 2 integers.
It takes two parameters: a and b, which are the numbers to be added.
Then returns the values
"""


def add_integer(a, b=98):
    """This is a function that returns the addition of 2 variables
    a (int): the first number
    b (int): the second number"""
    if isinstance(a, float) and isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int) or isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, float):
        raise TypeError("b must be an integer")
    return a + b
