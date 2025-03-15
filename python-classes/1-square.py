#!/usr/bin/python3

"""
This module defines a Square class.
"""


class Square:
    """
    A class that defines a square with a private instance attribute `size`.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
