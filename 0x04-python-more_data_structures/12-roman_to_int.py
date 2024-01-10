#!/usr/bin/python3

def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0
    if roman_string == None:
        return 0

    for numeral in reversed(roman_string):
        value = rom[numeral]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return str(total)
