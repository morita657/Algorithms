#!/bin/python

import math
import os
import random
import re
import sys

# search value in sorted array using binary search


def main(n, k, a):
    lb = -1
    ub = n
    while ub - lb > 1:
        mid = (lb + ub) / 2
        print("mid: ", mid)
        if a[mid] >= k:
            ub = mid
        else:
            lb = mid
    print(ub)


main(5, 3, [2, 3, 3, 5, 6])
