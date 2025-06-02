#!/usr/bin/python3
"""
This module provides a function to convert Python data structures
to JSON strings.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
        my_obj (any): The Python object to convert (e.g., dict,
        list, str, int, etc.).

    Returns:
        str: The JSON-formatted string representation of the object.

    Raises:
        TypeError: If the object is not JSON serializable.
    """
    json_str = json.dumps(my_obj)
    return json_str
