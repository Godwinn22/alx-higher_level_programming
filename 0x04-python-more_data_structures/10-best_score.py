#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = 0
    best_val = 0
    for key, val in a_dictionary.items():
        if val > best_val:
            best_key = key
            best_val = val
    return best_key
