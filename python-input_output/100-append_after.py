#!/usr/bin/python3
"""
Function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Searches for `search_string` in each line of `filename`,
    and inserts `new_string` after the line if found."""
    with open(filename, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(new_lines)
