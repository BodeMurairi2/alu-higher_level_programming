#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a class or a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """This function checks if an object is
    an instance of a class or a subclass.
    """
    return bool(isinstance(obj, a_class))
