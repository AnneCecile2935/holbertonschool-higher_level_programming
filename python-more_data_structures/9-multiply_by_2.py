#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Multiplies all values in a dictionary by 2.

    This function creates a new dictionary where each value from
    the input dictionary
    is multiplied by 2. The keys remain unchanged.

    Args:
        a_dictionary (dict): The dictionary whose values will be
        multiplied by 2.

    Returns:
        dict: A new dictionary with the same keys, but with each value
        multiplied by 2.

    Example:
        >>> multiply_by_2({"a": 1, "b": 2})
        {"a": 2, "b": 4}
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
