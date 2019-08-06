#!/bin/python

import math
import os
import random
import re
import sys
S = [1, 2, 4, 6, 8]
T = [3, 5, 7, 9, 10]
N = 5


def main():
    s = 0
    ans = 0
    for i in range(0, N):
        if s < S[i]:
            ans += 1
            s = T[i]
    return ans


print main()
