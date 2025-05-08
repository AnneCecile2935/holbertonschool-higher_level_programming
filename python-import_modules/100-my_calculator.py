#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    func = operators[operator]
    if operator == '/' and b == 0:
        print("Error : Division by zero")
        sys.exit(1)
    result = func(a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
