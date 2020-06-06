#!/bin/python3
'''
Title   : 2D Array - DS
Problem : https://www.hackerrank.com/challenges/ctci-ransom-note/problem
'''

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    a =  Counter(note) - Counter(magazine)
    if a:
        print("No")
    else:
        print("Yes")
