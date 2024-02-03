#!/usr/bin/python3
"""
This is a function that prints a text with 2 new lines after
each of these characters: ., ? and :
It takes one parameter: text
"""


def text_indentation(text):
    """This is a function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text: the text we are using
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for j in text:
        print(j, end="")
        if j in [':', '?', '.']:
            print("\n\n", end="")
