#!/usr/bin/python3
"""A module that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    This is a function returns the JSON representation of an object (string)
    Args:
        my_obj (any): the object we are to serialize
    """
    return json.dumps(my_obj)
