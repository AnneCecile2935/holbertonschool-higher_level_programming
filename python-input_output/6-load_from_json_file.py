#!/usr/bin/python3
"""
This module provides a function that create an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object represented by the JSON content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        json_file = json.load(f)
    return json_file
