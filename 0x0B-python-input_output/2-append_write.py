#!/usr/bin/python3
"""This module appends a string at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file (UTF8)
and returns the number of characters added.
    Args:
        filename: The name of the file to be created or overwritten.
        text: The texts
    """
    with open(filename, 'a', encoding="utf-8") as file_1:
        return file_1.write(text)
