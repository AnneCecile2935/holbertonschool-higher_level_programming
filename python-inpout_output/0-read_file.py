#!/usr/bin/python3
"""
This module provides a function to read and display the contents
of a text file.
"""
def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The path to the file to be read.
        Defaults to an empty string.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be accessed due
        to permission issues.
    """
    with open("my_file_0.txt", "rt") as f:
        print(f.read())
