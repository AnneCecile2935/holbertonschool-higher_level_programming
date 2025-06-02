#!/usr/bin/python3
"""
This module provides a function to convert a JSON string to a Python object.
"""


import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): A string containing a JSON-formatted
        representation of an object.

    Returns:
        object: The corresponding Python data structure
        (e.g., dict, list, etc.).
    """
    json_str = json.loads(my_str)
    return json_str
