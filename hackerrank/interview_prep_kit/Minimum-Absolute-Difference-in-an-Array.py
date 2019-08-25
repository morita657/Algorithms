#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.


def minimumAbsoluteDifference(arr):
    mini = 10**10
    arr.sort()
    for i in range(n - 1):
        # print arr[i], arr[i+1], i, i+1
        mini = min(mini, abs(arr[i] - arr[i + 1]))
    return mini


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
