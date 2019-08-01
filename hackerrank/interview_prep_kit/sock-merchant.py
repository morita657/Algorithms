#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}
    for sock in range(len(ar)):
        if ar[sock] in socks.keys():
            socks[ar[sock]]  +=1
        else:
            socks[ar[sock]] = 1
    cnt = 0
    for color in socks:
        cnt += socks[color]/2
    return cnt
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)


    fptr.write(str(result) + '\n')

    fptr.close()

