#!/usr/bin/python3

"""
This module creates a class Square.
"""


class Square:
    """
    A class that defines a square with a private instance attribute `size`.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            """
            Computes the area of the square.
            Returns:
                The area of the square.
            """
            return self.__size ** 2
