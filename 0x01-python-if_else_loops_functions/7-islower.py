#!/usr/bin/python3
def islower(c):
    first = ord('a')
    second = ord('z')
    third = ord(c)
    if chr(third) >= chr(first) and chr(third) <= chr(second):
        return True
    else:
        return False
