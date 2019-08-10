#!/bin/python

# Expedition
import math
import os
import random
import re
import sys


def main():
    N = 4
    L = 25
    P = 10
    A = [10, 14, 20, 21]
    B = [10, 5, 2, 4]
    loc = 0
    q = []
    gasoline = 0

    while P > 0:
        P -= 1
        loc += 1
        if loc == A[0]:
            gas = B[0]
            q.append(gas)
            B = B[1:]
        if loc == L:
            break
        if P == 0 and loc + 1 != L:
            q.sort()
            P += q[-1]
            gasoline += 1
    return gasoline


print(main())
