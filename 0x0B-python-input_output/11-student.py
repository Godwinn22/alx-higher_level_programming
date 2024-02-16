#!/usr/bin/python3
"""Defines a class Student that defines a student by their
first_name, last_name and age."""


class Student:
    """Represent the student class"""

    def __init__(self, first_name, last_name, age):
        """Defines a class Student that defines a student by their
        first_name, last_name and age.
        Args:
            first_name(str): the first name
            last_name(str): the last name
            age(int): the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self,  attrs=None):
        """returns a dictionary representation of a class
        """
        if attrs is None:
            return (self.__dict__)
        attr_dict = {}
        for attr in attrs:
            for val in self.__dict__:
                if attr == val:
                    attr_dict[attr] = self.__dict__[val]
        return attr_dict

    def reload_from_json(self, json):
        """a function that replaces all attributes of an instance.
        
        Args:
            json: a dictionnary
        """
        for key, value in json.items():
            setattr(self, key, value)