#!/usr/bin/python3
"""
This is a function that prints My name is <first name> <last name>
It takes two parameters: first_name and last_name]
"""


def say_my_name(first_name, last_name=""):
    """This is a function that prints My name is <first name> <last name>
    Args:
        first_name: the first name
        last_name: the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name)) 
