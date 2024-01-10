#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == None:
        return None

    max_num = my_list[0]

    for i in my_list[1:]:
        if i > max_num:
            max_num = i
    return max_num
