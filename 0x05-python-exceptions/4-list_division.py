#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    dividend, divisor = 0, 0
    try:
        for i in range(list_length):
            try:
                if (i < len(my_list_1)):
                    dividend = my_list_1[i]
                else:
                    dividend = 0
                    raise IndexError("out of range")
                    
                if (i < len(my_list_2)):
                    divisor = my_list_2[i]
                else:
                    divisor = 1
                    raise IndexError("out of range")
                
                # if not isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                #     raise TypeError("wrong type")
                # if divisor == 0:
                #     new_list.append(0)
                #     print("division by 0")
                # else:
                new_list.append(dividend / divisor)
            except IndexError:
                print("out of range")
                new_list.append(0)
            except TypeError:
                print("wrong type")
                new_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
    finally:
        return new_list