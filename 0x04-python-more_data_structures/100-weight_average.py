#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        sum1 = 0
        sum2 = 0
        for i in my_list:
            number1, number2 = i
            mul = number1 * number2
            sum1 += mul
            sum2 += number2
    return sum1 / sum2
