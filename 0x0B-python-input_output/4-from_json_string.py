#!/usr/bin/python3
"""Defines a module that creates a function that returns an object
(Python data structure) represented by a JSON string."""
import json


def from_json_string(my_str):
    """
    Defines a function that returns an object (Python data structure)
    represented by a JSON string.
    Args:
        my_str (str): the JSON string we are to deserialize
    """
    x = json.loads(my_str)
    return x
