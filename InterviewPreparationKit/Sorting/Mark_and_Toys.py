#!/bin/python3
'''
Title   : Mark and Toys
Problem : https://www.hackerrank.com/challenges/mark-and-toys/problem
'''

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    '''Returns an integer representing the
    maximum number of toys Mark can purchase
    - prices: Array with price of each toy
    - k: Money available to spend in toys'''

    prices.sort() # First, sort the list of prices
    toys = 0 # Number of toys
    spent_money = 0

    for toy_price in range(0, len(prices)):
        spent_money += prices[toy_price]
        toys += 1
        if spent_money + prices[toy_price + 1] >= k:
            return toys
