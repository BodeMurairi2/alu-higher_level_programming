#!/usr/bin/python3
# Print all possible different combinations of two digits.
# The two digits must be different.
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i != 8 or j != 9:
            print("{:d}{:d}, ".format(i, j), end="")
        else:
            print("{:d}{:d}".format(i, j))
