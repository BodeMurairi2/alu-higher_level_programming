#!/usr/bin/python3
# FizzBuzz


def fizzbuzz():
    '''This print numbers from 1 to 100
    for multiple of 3, print fizz
    for multiple of 5, print buzz
    for multiple of 3 and 5, print fizzbuzz'''

    for number in range(1, 101):
        if number % 3 == 0:
            print("Fizz", end="")
        elif number % 5 == 0:
            print("Buzz", end="")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end="")
        else:
            print("{:d}".format(number), end="")
