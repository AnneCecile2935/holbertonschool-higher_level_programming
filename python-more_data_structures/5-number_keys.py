#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary.

    This function calculates the total number of keys in the
    provided dictionary by using the `len()` function.

    Args:
        a_dictionary (dict): The dictionary whose keys are to be counted.

    Returns:
        int: The number of keys in the dictionary.

    Example:
        >>> number_keys({"a": 1, "b": 2, "c": 3})
        3
    """
    numbkey = len(a_dictionary)
    return (numbkey)
