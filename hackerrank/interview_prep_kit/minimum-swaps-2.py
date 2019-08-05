#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    swap = 0
    i = 0
    while i < len(arr):
        # Bug in input data which violates problem constraints
        if arr[i] == (i + 1):
            i += 1
            continue
        print i, arr[arr[i] - 1], arr[i], arr
        arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        swap += 1
    return swap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
