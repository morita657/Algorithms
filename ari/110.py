#!/bin/python

# Dijkstra
import math
import os
import random
import re
import sys

# is prime?


def main(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


print(main(10))
print(main(53))
print(main(295927))

# divisor


def main(num):
    res = []
    for i in range(2, num):
        if i * i <= num:
            if num % i == 0:
                res.append(i)
                if i != num / i:
                    res.append(num / i)
    return not len(res)


print(main(10))
print(main(53))
print(main(295927))

# prime factorization


def main(num):
    res = []
    for i in range(2, num):
        if i * i <= num:
            while num % i == 0:
                num //= i
                res.append(i)
    return not len(res)


print(main(10))
print(main(53))
print(main(295927))
