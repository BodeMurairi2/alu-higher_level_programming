#!/usr/bin/python3
# FizzBuzz


def fizzbuzz():
    '''This print numbers from 1 to 100
    for multiple of 3, print fizz
    for multiple of 5, print buzz
    for multiple of 3 and 5, print fizzbuzz'''

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
