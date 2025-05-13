#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of a specific element in a list with a new value.

    This function iterates through each element in the provided
    list and replaces
    any occurrence of the specified 'search' element with
    the 'replace' value.
    If the element does not match the 'search' value,
    it is appended to the new list unchanged.

    Args:
        my_list (list): The original list of elements.
        search: The value to be searched and replaced.
        replace: The value to replace the 'search' element.

    Returns:
        list: A new list with the specified replacements applied.
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
