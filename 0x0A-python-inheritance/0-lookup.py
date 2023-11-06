#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of all available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list of strings with  names of all available attributes and methods.
    """

    attrs = []
    for name in dir(obj):
        if not name.startswith('__'):
            attrs.append(name)
    return attrs
