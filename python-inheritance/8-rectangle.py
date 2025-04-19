#!/usr/bin/python3
"""
This module contains a class BaseGeometry
"""


class BaseGeometry:
    """This is class defines a base geometry"""
    def __init__(self, width, height):
        """Initialize width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def area(self):
        """This method raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
