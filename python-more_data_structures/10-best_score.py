#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the highest value in a dictionary.

    This function checks if the dictionary is not empty.
    If it contains elements, it finds the key with the highest associated
    value and returns it. If the dictionary is empty, it returns `None`.

    Args:
        a_dictionary (dict): A dictionary where keys are associated with
        numerical values.

    Returns:
        The key with the highest value in the dictionary, or `None` if the
        dictionary is empty.

    Example:
        >>> best_score({"a": 90, "b": 95, "c": 85})
        "b"
    """
    if a_dictionary:
        key_max_value = max(a_dictionary, key=a_dictionary.get)
        return (key_max_value)
    return None
