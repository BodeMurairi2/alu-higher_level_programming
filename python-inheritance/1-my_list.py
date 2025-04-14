#!/usr/bin/python3
"""
This module contains a class with method that prints a sorted list
"""


class MyList(list):
    """This class inherits from list and adds a method to
    print a sorted list
    """
    def print_sorted(self):
        """Prints the list in sorted order"""
        print(sorted(self), ascending=True)
