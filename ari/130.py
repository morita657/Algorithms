#!/bin/python

import math
import os
import random
import re
import sys

N = 4
K = 11
L = [8.02, 7.43, 4.57, 5.39]


def C(x):
    num = 0
    for i in range(N):
        num += int(L[i] / x)
    return num >= K


def solve():
    lb = 0
    # ub = float("inf")
    ub = 100000
    for i in range(100):
        mid = (lb + ub) / 2
        if C(mid):
            lb = mid
        else:
            ub = mid
    return math.floor(ub * 100) / 100


def main():
    return solve()


print(main())
