#!/usr/bin/python3
"""This module writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    A function writes a string to a text file (UTF8)
    and returns the number of characters written.
    Args:
        filename: The name of the file to be created or overwritten.
        text: The texts
    """
    with open(filename, 'w', encoding="utf-8") as file_1:
        return file_1.write(text)
