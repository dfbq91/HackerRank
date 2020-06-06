#!/bin/python3
'''
Title   : Left Rotation
Problem : https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
'''

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    new_array = []
    var = d

    while len(new_array) != len(a):
        new_array.append(a[var])
        if var == len(a) - 1:
            var = 0
        else:
            var += 1
    print(new_array)
    return (new_array)
