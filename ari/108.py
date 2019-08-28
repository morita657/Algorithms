#!/bin/python

# Dijkstra
import math
import os
import random
import re
import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# (5, 3)
print(gcd(1, 11))
print(gcd(5, 3))
