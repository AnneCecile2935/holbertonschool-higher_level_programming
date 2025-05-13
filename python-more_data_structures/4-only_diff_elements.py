#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns the elements that are in one set but not in the other.

    This function computes the symmetric difference between two sets,
    meaning it
    returns the elements that are unique to each set. It does this by
    subtracting
    the elements of one set from the other and then combining the results.

    Args:
        set_1 (set): The first set of elements.
        set_2 (set): The second set of elements.

    Returns:
        set: A set containing the elements that are in either set_1 or set_2,
        but not in both.

    Example:
        >>> only_diff_elements({1, 2, 3}, {2, 3, 4})
        {1, 4}
    """
    return (set_1 - set_2) | (set_2 - set_1)
