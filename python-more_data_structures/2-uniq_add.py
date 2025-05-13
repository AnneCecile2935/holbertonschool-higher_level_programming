#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    This function converts the input list to a set to remove duplicate elements
    and then calculates the sum of the unique values.

    Args:
        my_list (list): A list of integers. Duplicates are ignored.

    Returns:
        int: The sum of all unique integers in the list.

    Example:
        >>> uniq_add([1, 2, 3, 2, 4, 1])
        10  # (1 + 2 + 3 + 4)
    """
    my_set = set(my_list)
    total = sum(my_set)
    return total
