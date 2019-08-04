# algorithm quicksort(A, lo, hi) is
#     if lo < hi then
#         p := partition(A, lo, hi)
#         quicksort(A, lo, p - 1)
#         quicksort(A, p + 1, hi)

# algorithm partition(A, lo, hi) is
#     pivot := A[hi]
#     i := lo
#     for j := lo to hi - 1 do
#         if A[j] < pivot then
#             swap A[i] with A[j]
#             i := i + 1
#     swap A[i] with A[hi]
#     return i
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        minimumSwaps(arr, lo, p - 1)
        minimumSwaps(arr, p + 1, hi)


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in arr[lo:hi]:
        if arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i]
    arr[i] = arr[hi]
    arr[hi] = temp
    return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr, min(arr), max(arr))

    fptr.write(str(res) + '\n')

    fptr.close()
