#!/usr/bin/python3
"""
This module checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    This function checks if an object is an instance of a class
    """
    return bool(isinstance(obj, a_class) and type(obj) is a_class)
