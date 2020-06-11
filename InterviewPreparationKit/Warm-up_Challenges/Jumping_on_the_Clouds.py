#!/bin/python3

'''
Title   : Jumping on the Clouds
Problem : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    '''Returns the minimum number of jumps required, as an integer.
    c: an array of binary integers'''

    i = 0 # pointer position
    moves = 0 # number of jumps

    while i < len(c) - 1:
        if i < len(c) - 2:
            if c[i + 1] == 0 and c[i + 2] == 0 or c[i + 1] == 1:
                i += 2
            else:
                i += 1

        else:
            if c[i + 1] == 0:
                i += 1
            else:
                return moves
        moves += 1

    return moves
