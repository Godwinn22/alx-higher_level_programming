#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    updated_one = a_dictionary.copy()
    for key, val in updated_one.items():
        updated_one[key] = int(val) * 2
    return updated_one
