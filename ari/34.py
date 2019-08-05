#!/bin/python

import math
import os
import random
import re
import sys

n = 4
a = [1, 2, 4, 7]
k = 13


def dfs(i, sum):
    if i == n:
        return sum == k
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + a[i]):
        return True
    return False


def main():
    # f = open("input.txt", "r")
    # contents = f.read().split()
    if dfs(0, 0):
        print 'YES'
    else:
        print 'NO'
    return 0


print main()
