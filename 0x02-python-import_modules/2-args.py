#!/usr/bin/python3
if __name__ == "__main__":
    x = 1
    from sys import argv
    arg_len = len(argv) - 1
    if (arg_len == 0):
        print("{} arguments.".format(arg_len))
    elif (arg_len == 1):
        print("{} argument:".format(arg_len))
    else:
        print("{} arguments:".format(arg_len))
    while x <= arg_len:
        print("{}: {}".format(x, argv[x]))
        x += 1
