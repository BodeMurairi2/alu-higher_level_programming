#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle."""


class Rectangle():
    """this class represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


class Square(Rectangle):
    """this class represents a square using Rectangle"""
    def __init__(self, size):
        """Initialize a new square """
        if isinstance(size, int) and size > 0:
            self.__size = size
        else:
            raise TypeError("size must be a positive integer")

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
