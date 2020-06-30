#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    '''Return the substring of k length that contains the most vowels'''
    temp_nvowels = 0
    nvowels = 0
    sub_string = ''
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(0, len(s) - k + 1):
        temp_nvowels += s[i:i + k].count(vowels[0])
        temp_nvowels += s[i:i + k].count(vowels[1])
        temp_nvowels += s[i:i + k].count(vowels[2])
        temp_nvowels += s[i:i + k].count(vowels[3])
        temp_nvowels += s[i:i + k].count(vowels[4])             
        if temp_nvowels > nvowels:
            nvowels = temp_nvowels
            sub_string = s[i:i + k]
        temp_nvowels = 0
        
    if nvowels > 0:
        return sub_string
    else:
        return 'Not found!'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()
