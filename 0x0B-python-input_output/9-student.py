#!/usr/bin/python3
"""Defines a class Student that defines a student by their
first_name, last_name and age."""


class Student:
    """Defines a class Student that defines a student by their
    first_name, last_name and age.
    Args:
        first_name(str): the first name
        last_name(str): the last name
        age(int): the age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
