#!/usr/bin/python3
# This script imports the add function from add_0.py

from add_0 import add


def main():
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}")


if __name__ == "__main__":
    main()
