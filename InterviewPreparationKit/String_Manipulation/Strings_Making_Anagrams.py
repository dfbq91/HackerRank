#!/bin/python3
'''
Title   : Strings: Making Anagrams
Problem : https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
'''

import math
import os
import random
import re
import sys
from string import ascii_lowercase


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    '''Count number of times a lowercase letter is in both
    strings and rest them. The rest result gives number of times
    that letter must be deleted to make an anagram
    - a: a string
    - b: a string'''

    count_a  = 0
    count_b = 0
    count = 0

    # Iterates alphabet in lowercase
    for i in ascii_lowercase:
        # Count number of times that letter i is on string a and b
        # and assign it to the count_a and count_b
        count_a = a.count(i)
        count_b = b.count(i)

        # Rest both variables to know the number of times a letter
        # must be deteled to make an anagram
        count += abs(count_a - count_b)

    return count
