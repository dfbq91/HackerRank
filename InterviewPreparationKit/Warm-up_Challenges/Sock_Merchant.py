#!/bin/python3
'''
Title   : Sock_Merchant
Problem : https://www.hackerrank.com/challenges/sock-merchant/problem
'''

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    '''Returns an integer representing the number
    of matching pairs of socks that are available'''
    pairs = 0
    j = 1

    if len(ar) == 0:
        return pairs

    while len(ar) > 1:
        if ar[0] == ar[j]:
            ar.pop(j)
            ar.pop(0)
            pairs +=1
            j = 1
        elif j < len(ar) - 1:
            j += 1
        else:
            ar.pop(0)
            j = 1
    return pairs
