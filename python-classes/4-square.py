#!/usr/bin/python3

"""
Square module
"""


class Square:
    """
    This class represents a square
    Args:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a new square
        Args:
            size (int): The size of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def size(self):
        """
        Getter method for size
        Returns:
            The size of the square
        """
        return self.__size

    def area(self):
        """
        Computes the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2
