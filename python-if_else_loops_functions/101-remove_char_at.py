#!/usr/bin/python3
# This function removes a string at a specific index


def remove_char_at(str, n):
    if n >= 0:
        new_str = str[:n] + str[n + 1:]
        return new_str
    else:
        return str
