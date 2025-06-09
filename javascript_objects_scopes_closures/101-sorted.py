#!/usr/bin/python3

from data_101 import content

new_dict = {}

for key, value in content.items():
    str_val = str(value)
    str_key = str(key)
    if str_val not in new_dict:
        new_dict[str_val] = []
    new_dict[str_val].append(str_key)

print(new_dict)
