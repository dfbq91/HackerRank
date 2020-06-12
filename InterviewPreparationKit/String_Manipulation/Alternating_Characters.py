#!/bin/python3
'''
Title   : Alternating Characterers
Problem : https://www.hackerrank.com/challenges/alternating-characters/problem
'''

import math
import os
import random
import re
import sys


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    for i in range(0, len(s)-1):
        if i == 0:
            if s[i] == s[i + 1]:
                count += 1
        elif i != 0:
            if s[i] == s[i + 1]:
                count += 1
    print(count)
    return(count)
