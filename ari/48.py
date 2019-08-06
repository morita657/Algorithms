#!/bin/python

import math
import os
import random
import re
import sys

N = 6
R = 10
X = [1, 7, 15, 20, 30, 50]


def main():
    count = 0
    current = X[0]
    i = 0
    range = []
    while i < len(X):
        if X[i] < current + R:
            i += 1
            range.append(i)
        else:
            current = X[range[-1]]
            count += 1
    return count


print main()
