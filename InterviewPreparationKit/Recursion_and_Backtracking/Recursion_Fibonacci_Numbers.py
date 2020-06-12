#!/bin/python3
'''
Title   : Recursion: Fibonacci Numbers
Problem : https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
'''

def fibonacci(n):
    '''return the nth element in the Fibonacci sequence.
    - n: the integer index of the sequence to return'''

    # If the value is cached, return it
    fibonacci_cache = {} # Memoization
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    if n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value
