#!/usr/bin/python3
"""
append_after module

This module provides a function `append_after` which allows inserting
a given string into a file immediately after each line that contains
a specified search string.

It is useful for programmatically updating text files (such as configuration
files, scripts, or documentation) where new content needs to be inserted
conditionally after specific lines.

Functions:
    append_after(filename="", search_string="", new_string=""):
        Inserts a new line after lines containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text (new_string) into a file after every line
    that contains a specific search string (search_string).

    Args:
        filename (str): The path to the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each matching line.

    Returns:
        None

    Note:
        - The function overwrites the original file with the updated content.
        - It uses the 'with' statement for file operations.
        - It does not handle exceptions related to file permissions or missing
        files.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w") as d:
        d.writelines(new_lines)
