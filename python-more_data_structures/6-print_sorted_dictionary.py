#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints all keys and values of a dictionary, sorted by the keys.

    This function retrieves all the keys of the dictionary, sorts them
    in ascending order, and then prints each key with its corresponding value
    in the format "key: value".

    Args:
        a_dictionary (dict): The dictionary whose keys and values
        will be printed.

    Returns:
        None: This function prints the sorted keys and values and does not
        return anything.

    Example:
        >>> print_sorted_dictionary({"b": 2, "a": 1, "c": 3})
        a: 1
        b: 2
        c: 3
    """
    keys = a_dictionary.keys()
    sorted_keys = sorted(keys)
    for key in sorted_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")
