#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default is 98).

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.

    Examples:
        >>> add_integer(2, 3)
        5
        >>> add_integer(100)
        198
        >>> add_integer(2.5, 3)
        5
        >>> add_integer(2.5, "3")
        Traceback (most recent call last):
            ...
        TypeError: b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
