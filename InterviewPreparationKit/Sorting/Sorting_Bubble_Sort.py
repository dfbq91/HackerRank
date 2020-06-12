#!/bin/python3
'''
Title   : Sorting: Bubble Sort
Problem : https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
'''

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    '''Prints three lines: number of swaps to sort the array,
    first element and last element of the sorted array
    - a: an array of integers'''

    largo = len(a)
    swaps = 0

    for i in range(0, largo):
        for j in range(i, largo):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                swaps += 1

    print("Array is sorted in {} swaps.".format(swaps))
    print(("First Element: {}").format(a[0]))
    print(("Last Element: {}").format(a[largo-1]))
