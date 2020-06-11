#!/bin/python3

'''
Title   : Counting Valleys
Problem : https://www.hackerrank.com/challenges/counting-valleys/problem
'''

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    '''Returns an integer that denotes the
    number of valleys Gary traversed.
    n: the number of steps Gary takes
    s: a string describing his path'''

    var = 0
    was_negative = False
    valley = 0

    for x in s:
        if x == 'D':
            var -= 1
        elif x == 'U':
            var +=1
        if var < 0:
            was_negative = True
        if var == 0 and was_negative == True:
            valley += 1
            was_negative = False
    return valley
