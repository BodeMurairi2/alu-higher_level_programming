#!/usr/bin/python3
# check for lowercase character
def islower(c):
    '''This function checks for lowercase character.'''
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
