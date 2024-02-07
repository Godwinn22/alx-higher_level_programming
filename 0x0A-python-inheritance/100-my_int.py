#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """Defines a class MyInt that inherits from the int object"""
    def __eq__(self, num):
        """Returns the inverted form of !="""
        return int(self) != int(num)
    
    def __ne__(self, num):
        """Returns the inverted form of !="""
        return int(self) == int(num)        
