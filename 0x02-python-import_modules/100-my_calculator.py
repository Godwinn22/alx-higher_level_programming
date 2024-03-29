#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    import sys
    num_args = len(sys.argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and / ")
        sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
