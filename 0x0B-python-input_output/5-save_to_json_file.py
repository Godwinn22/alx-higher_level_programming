#!/usr/bin/python3
"""This module defines a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Defines a function that writes an Object to a text file,
    using a JSON representation
    Args:
        my_obj: the object
        filename: the file name
    """
    with open(filename, 'w', encoding="utf-8") as f:
        x = json.dumps(my_obj)
        return f.write(x)
