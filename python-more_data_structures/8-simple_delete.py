#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key-value pair from a dictionary if the key exists.

    This function checks if the specified key is present in the dictionary.
    If the key is found, the corresponding key-value pair is removed.
    If the key is not found, the dictionary remains unchanged.

    Args:
        a_dictionary (dict): The dictionary from which a key-value pair
        will be deleted.
        key (str, optional): The key to be deleted from the dictionary.
        Defaults to an empty string.

    Returns:
        dict: The updated dictionary after the key-value pair has been removed
        (if the key exists).

    Example:
        >>> simple_delete({"a": 1, "b": 2}, "a")
        {"b": 2}
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
