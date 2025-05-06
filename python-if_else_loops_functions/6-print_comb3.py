#!/usr/bin/python3
for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        print(
            "{:02}".format(digit1 * 10 + digit2),
            end=", " if digit1 != 8 or digit2 != 9 else "\n")
