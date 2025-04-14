#!/usr/bin/python3


"""This module contains a function that returns the list of available
    attributes and methods of an object.
    The function is called lookup.
    """


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to look up.

    Returns:
        A list of strings representing the names of the attributes and
        methods of the object.
    """
    return dir(obj)
