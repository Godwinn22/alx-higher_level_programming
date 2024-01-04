#!/usr/bin/python3
def remove_char_at(input_str, n):
    # Check if n is a valid index
    if 0 <= n < len(input_str):
        result = ""
        for i in range(len(input_str)):
            if i != n:
                result += input_str[i]
        return result
    else:
        return input_str
