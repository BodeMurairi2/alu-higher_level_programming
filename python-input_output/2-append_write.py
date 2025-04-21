#!/usr/bin/python3
"""Module that contains a function that appends
a string at the end of a text file"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file
    and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
