#!/usr/bin/python3
# This script prints a string in uppercase


def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{:c}".format(c), end="")
    print()
