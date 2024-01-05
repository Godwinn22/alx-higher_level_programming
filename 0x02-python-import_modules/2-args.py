#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    num_args = len(sys.argv)

    print("{} ".format(num_args - 1), end="")
    if num_args == 1:
        print("arguments.")
    elif num_args - 1 > 1:
        print("arguments:")
    else:
        print("argument:")
    for i in range(1, num_args):
        print("{}: {}".format(i, sys.argv[i]))
