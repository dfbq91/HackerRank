#!/bin/python3
'''
Title   : Minimum Absolute Difference in an Array
Problem : https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
'''

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    '''Returns an integer that represents the minimum
    absolute difference between any pair of elements.
    - n: an integer that represents the length of arr
    - arr: an array of integers'''

    # checks if an element exists more than once
    if len(arr) != len(set(arr)):
        return 0

    # Sort and iterate doing a rest and getting the minimal number
    arr.sort()
    min = 10**20
    for i in range(0, len(arr) - 1):
        if min > abs(arr[i] - arr[i + 1]):
            min = abs(arr[i] - arr[i + 1])
    return min
