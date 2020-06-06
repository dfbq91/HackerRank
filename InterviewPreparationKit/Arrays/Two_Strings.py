#!/bin/python3
'''
Title   : 2D Array - DS
Problem : https://www.hackerrank.com/challenges/two-strings/problem
'''

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    print(s1)
    print(s2)
    result = dict(Counter(s1) & Counter(s2))
    print(result)
    if result:
        return ("YES")
    else:
        return ("NO")
