#!/usr/bin/python3
# This script checks for uppercase characters in a string

def uppercase(str):
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90:
            return True
    return False
