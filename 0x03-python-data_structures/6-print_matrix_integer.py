#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for val, j in enumerate(i):
            if val < len(i) - 1:
                print("{}".format(j), end=" ")
            else:
                print("{}".format(j), end="")
        print()
