#!/usr/bin/python3
"""
This module provides a function toappends a string at the end of the text file
"""


def append_write(filename="", text=""):
    """
    Append a string to a text file (UTF8) and returns the number of characters
    added.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
