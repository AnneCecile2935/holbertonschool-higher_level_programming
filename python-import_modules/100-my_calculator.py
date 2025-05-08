#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul
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
        print("Error : Divivsion by zero")
        sys.exit(1)
    result = func(a, b)
    print(f"{a} {operator} {b} = {result}")
