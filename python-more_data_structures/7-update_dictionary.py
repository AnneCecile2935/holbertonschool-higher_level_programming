#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary by adding a key-value pair or modifying an existing
    key.

    This function updates the dictionary with the specified key and value.
    If the key already exists in the dictionary, its value will be updated.
    If the key does not exist, it will be added with the provided value.

    Args:
        a_dictionary (dict): The dictionary to be updated.
        key: The key to be added or updated.
        value: The value associated with the key.

    Returns:
        dict: The updated dictionary with the new or modified key-value pair.

    Example:
        >>> update_dictionary({"a": 1, "b": 2}, "c", 3)
        {"a": 1, "b": 2, "c": 3}
    """
    a_dictionary[key] = value
    return a_dictionary
