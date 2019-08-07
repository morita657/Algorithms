#!/bin/python

import math
import os
import random
import re
import sys

n = 4
# (w, v)
s = [(2, 3), (1, 2), (3, 4), (2, 2)]
W = 5
total = 0
weight = 0

res = 0


def dfs(weight, total, i, s):
    if i == n:
        return total
    if s[i][0] > W:
        res = dfs(weight, total, i + 1, s)
    else:
        res = max(dfs(total + s[i][1], weight + s[i][0],
                      i + 1, s), dfs(total, weight, i + 1, s))
    return res


def main():
    print dfs(0, 0, 0, s)
    return 0


main()
