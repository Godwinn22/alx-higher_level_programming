#!/usr/bin/python3
def uppercase(str):
    upper_i = ''
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            upper_i += chr(ord(i) - 32)
        else:
            upper_i += i
    print("{}".format(upper_i))
