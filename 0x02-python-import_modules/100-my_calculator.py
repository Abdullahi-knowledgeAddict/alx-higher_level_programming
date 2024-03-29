#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    arglen = len(argv)
    if arglen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    argv[1] = int(argv[1])
    argv[3] = int(argv[3])
    if argv[2] == "+":
        print(f"{argv[1]} + {argv[3]} = {add(argv[1], argv[3])}")
    elif argv[2] == "-":
        print(f"{argv[1]} - {argv[3]} = {sub(argv[1], argv[3])}")
    elif argv[2] == "/":
        print(f"{argv[1]} / {argv[3]} = {div(argv[1], argv[3])}")
    elif argv[2] == "*":
        print(f"{argv[1]} * {argv[3]} = {mul(argv[1], argv[3])}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
