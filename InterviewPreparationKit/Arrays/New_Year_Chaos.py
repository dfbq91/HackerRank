#!/bin/python3
'''
Title   : New Year Chaos
Problem : https://www.hackerrank.com/challenges/new-year-chaos/problem
'''

import math
import os
import random
import re
import sys


def minimumBribes(q):
    '''Prints an integer representing the minimum number of bribes
    necessary, or Too chaotic if the line configuration is not possible'''
    bribes = 0

    # Start at the end and go back to the beginning
    for i in range(len(q) - 1, -1, -1):

        # Compare original position with current position of the
        # number knowing if the number was moved more than 2 times
        if (q[i] - (i + 1) > 2):
            print("Too chaotic")
            return

        # Checks how many times q[i] changed
        # its original position
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)
