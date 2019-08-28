#!/bin/python

import math
import os
import random
import re
import sys

# Sieve of Eratosthenes


def main(num):
    candidates = []
    for i in range(1, num + 1):
        candidates.append(i)
    for i in range(2, len(candidates)):
        for j in range(i, len(candidates)):
            if i * j in candidates:
                candidates.pop(candidates.index(j * i))
    return candidates


print(main(20))

# segment sieve
# a <= N < b


def main(a, b):
    measurement = []
    candidates = []
    # find all of the candidates in the segment
    for i in range(a, b):
        candidates.append(i)
    # define the range to measure if the candidate is the prime
    for i in range(2, int(math.sqrt(b))):
        measurement.append(i)
    # find the non prime numbers and delete them
    for i in range(2, b):
        for j in range(i, b):
            if i * j in candidates:
                candidates.pop(candidates.index(j * i))
    return candidates


print(main(22, 37))
