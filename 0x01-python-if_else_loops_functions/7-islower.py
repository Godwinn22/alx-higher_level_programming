#!/usr/bin/python3
def islower(c):
    char_c = chr(ord(c))
    if char_c >= chr(ord('a')) and char_c <= chr(ord('z')):
        return True
    else:
        return False
