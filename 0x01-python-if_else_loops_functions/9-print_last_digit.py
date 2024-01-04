#!/usr/bin/python3
def print_last_digit(number):
    last_digit = ''
    if number < 0:
        last_digit = abs(number) % 10
        print("{}".format(last_digit), end="")
    else:
        print("{}".format(number % 10), end="")
    return last_digit
