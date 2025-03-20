#!/usr/bin/python3

'''
This module handles the rectangle form
'''


class Rectangle:
    '''
    This class handles the rectangle form
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value  # Name-mangled attribute

    @property
    def height(self):
        return self.__height  # Name-mangled attribute

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


my_rectangle = Rectangle(4, 0)
print(f"{my_rectangle.width} - {my_rectangle.height}")
