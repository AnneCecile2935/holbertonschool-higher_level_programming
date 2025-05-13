#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Finds the common elements between two sets.

    This function returns a new set containing the elements that are present
    in both input sets using the intersection operator (`&`).

    Args:
        set_1 (set): The first set of elements.
        set_2 (set): The second set of elements.

    Returns:
        set: A set containing the common elements between set_1 and set_2.

    Example:
        >>> common_elements({1, 2, 3}, {2, 3, 4})
        {2, 3}
    """
    return set_1 & set_2
