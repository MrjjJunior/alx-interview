#!/usr/bin/python3
""" Python Minimum Operations """

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations = operations + divisor
            n = n // divisor
        divisor = divisor + 1

    return operations
