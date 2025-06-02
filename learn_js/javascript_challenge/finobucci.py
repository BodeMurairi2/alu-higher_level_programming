#!/usr/bin/python3

def fibonacci_sum_even(n):
    sequence = []
    a = 0
    b = 1
    for i in range(n):
        sequence.append(a)
        a = b
        b = a + b
    
    sum_values = 0
    for num in sequence:
        if (num < 4000000) and (num % 2 == 0):
            sum_values = sum_values + num

    return sum_values


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter a number: "))
list_sequences = [fibonacci_recursive(i) for i in range(n)]
sum_even = 0
for i in list_sequences:
    if i < 4000000 and i % 2 == 0:
        sum_even += i

print(sum_even)
