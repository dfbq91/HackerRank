#!/usr/bin/python3
'''
Title     : 2D Array - DS
Problem   : https://www.hackerrank.com/challenges/2d-array/problem
'''

import math
import os
import random
import re
import sys
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    curr_count = 0
    highest = -999999
    for x in range(1, len(arr) - 1):
        for y in range(1, len(arr[x]) - 1):
            curr_count+= arr[x - 1][y - 1]
            curr_count+= arr[x - 1][y]
            curr_count+= arr[x - 1][y + 1]
            curr_count+= arr[x][y]
            curr_count+= arr[x + 1][y - 1]
            curr_count+= arr[x + 1][y]
            curr_count+= arr[x + 1][y + 1]
            if curr_count > highest:
                highest = curr_count
            curr_count = 0

    print(highest)
    return highest
