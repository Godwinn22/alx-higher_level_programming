#!/usr/bin/python3
""" This is a module that reads a file"""
import sys


def read_file(filename=""):
    """
    This function reads a file and prints the result to stdout
    Args:
        filename: the name of the file.
    """
    with open(filename, 'r', encoding="utf-8") as file_1:
        a = file_1.read()
        sys.stderr.write("{}\n".format(a))
