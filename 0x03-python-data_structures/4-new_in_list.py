#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]  # or i can use the my_list.copy()
    if idx < 0:
        return new_list
    if idx >= len(my_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
