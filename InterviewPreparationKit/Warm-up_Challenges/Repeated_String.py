#!/bin/python3

'''
Title   : Repeated String
Problem : https://www.hackerrank.com/challenges/repeated-string/problem
'''

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    '''Returns an integer representing the number of occurrences
    of a in the prefix of length n in the infinitely repeating string.
    s: a string to repeat
    n: the number of characters to consider'''

    a_count = s.count('a') # Counts number of 'a' in the initial string

    # Know the number of a, we can be close to the number
    # of 'a' multiplying by n//3.
    a_count *= n//len(s)

    # The module of n%len is what is missing for the string to be n
    a_count += s[0:n%len(s)].count('a')
    return a_count
