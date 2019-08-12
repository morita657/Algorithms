#!/bin/python

import math
import os
import random
import re
import sys

n = 3
k = 2
w = [(2, 2), (5, 3), (2, 1)]
y = []
for i in range(n):
    y.append(0)


def C(x):
    for i in range(n):
        print('w[i][0] - x * w[i][1]: ', w[i][0] - x * w[i][1])
        y[i] = w[i][0] - x * w[i][1]
        y.sort()
    sum = 0
    for i in range(k):
        sum += y[n - i - 1]
    return sum >= 0


def solve():
    lb = 0
    ub = 100000
    for i in range(100):
        # print('(lb + ub) / 2: ', float((lb + ub) / 2))
        mid = float((lb + ub) / 2)
        if C(mid):
            lb = mid
        else:
            ub = mid
    return float(ub)


def main():
    return solve()


print(main())
