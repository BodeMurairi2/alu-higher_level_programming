#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_numb = 0
    for i in my_list:
        if i > max_numb:
            max_numb = i
    return "{:d}".format(max_numb)
