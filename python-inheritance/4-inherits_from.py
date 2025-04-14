#!/usr/bin/python3
"""
This module contains a function that
checks if an object is an instance of a class
"""


def inherits_from(obj, a_class):
    """This function checks if an object is
    an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
