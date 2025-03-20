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

    def width(self):

        if not isinstance(self.width, int):
            raise TypeError("width must be an integer")
        elif self.width < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.width

    def height(self):
        if not isinstance(self.height, int):
            raise TypeError("height must be an integer")
        elif self.height < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.height
