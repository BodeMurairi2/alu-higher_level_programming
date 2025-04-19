#!/usr/bin/python3
"""
This module contains a class BaseGeometry
"""


class BaseGeometry:
    """This is class defines a base geometry"""
    def area(self):
        """This method raises an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates value as integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
