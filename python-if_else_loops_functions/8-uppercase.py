#!/usr/bin/python3
# This function changes a str from lower to uppercase


def uppercase(str):
    new_str = ""
    for i in str:
        if i >= 'a' and i <= 'z':
            new_str = new_str + chr((ord(i) - 32))
        else:
            new_str = new_str + i

    print("{}".format(new_str))
