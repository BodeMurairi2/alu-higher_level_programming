#!/usr/bin/python3
# This script the ASCII Alphabet in reverse order.
# alternating lower and uppercase letter


for i in range(122, 96, -1):
    print("{:c}".format(i if (i % 2 == 0) else (i - 32)), end='')
