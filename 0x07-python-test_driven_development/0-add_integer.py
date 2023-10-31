#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Return: the integer addition of a and b.

    Float or int  arguments are allocated to ints before addition is performed.
    Second int Defaults to 98.

    Raises:
        TypeError: If either of a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
