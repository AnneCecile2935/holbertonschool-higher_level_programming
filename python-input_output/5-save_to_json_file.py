#!/usr/bin/python3
"""
This module provides a function to save a Python object to a file
using its JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using its
    JSON representation.

    Args:
        my_obj (any): The Python object to serialize and save.
        filename (str): The name of the file to write to.

    The function overwrites the file if it already exists.
    It does not return anything.
    """
    with open(filename, "w", encoding='utf-8') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
