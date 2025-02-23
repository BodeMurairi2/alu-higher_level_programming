#!/usr/bin/python3
# This script prints a string in uppercase

def uppercase(str):
    """Print a string in uppercase."""
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        result += "{:c}".format(c)
    print(result)
