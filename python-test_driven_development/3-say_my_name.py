#!/usr/bin/python3
"""
This module provides a function to print a full name
using the provided first name and optional last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name. Must be a string.
        last_name (str, optional): The last name. Must be
        a string. Defaults to "".

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe
        >>> say_my_name("Alice")
        My name is Alice
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    first_name = first_name.strip()
    last_name = last_name.strip()
    if not first_name and not last_name:
        print("My name is")
    elif not first_name:
        print(f"My name is {last_name}")
    elif not last_name:
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
