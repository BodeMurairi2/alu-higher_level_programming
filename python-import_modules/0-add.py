#!/usr/bin/python3
# This script imports the add function from add_0.py


if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b))) # Use add(a, b) only once
