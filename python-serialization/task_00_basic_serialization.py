#!/usr/bin/env python3
"""
task_00_basic_serialization.py

Module for basic JSON serialization and deserialization in Python.

This module provides two functions:
1. serialize_and_save_to_file(data, filename)
2. load_and_deserialize(filename)

Functions:
----------
- serialize_and_save_to_file(data, filename):
    Serializes a Python dictionary and saves it to a JSON file.
    If the file already exists, it will be overwritten.

- load_and_deserialize(filename):
    Loads and deserializes JSON data from a file into a Python dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Parameters:
    -----------
    data : dict
        A Python dictionary containing the data to serialize.
    filename : str
        The name of the JSON file to write to. Overwrites if the file exists.

    Returns:
    --------
    None
    """
    with open(filename, "w", encoding="UTF8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Parameters:
    -----------
    filename : str
        The name of the JSON file to read from.

    Returns:
    --------
    dict
        A Python dictionary representing the JSON data.
    """
    with open(filename, "r", encoding="UTF8") as f:
        return json.load(f)
