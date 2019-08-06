#!/bin/python

import math
import os
import random
import re
import sys

n = 4
s = [(2, 3), (1, 2), (3, 4), (2, 2)]  # w,v
W = 5
res = 0


def knapsack(i,  weight):
    if i == n:
        res = 0
    elif weight < s[i][0]:
        res = knapsack(i + 1, weight)
    else:
        res = max(
            knapsack(i + 1, weight - s[i][0]) + s[i][1],
            knapsack(i + 1, weight)
        )
    return res


def main():
    print(knapsack(0, W))
    return 0


main()
