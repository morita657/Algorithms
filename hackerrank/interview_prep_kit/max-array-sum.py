#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    incl = 0
    excl = 0
    temp=0
    for i in range(len(arr)):
    # for(int i = 0; i < arr.size(); i++) {
        temp = incl;
        incl = max(arr[i]+excl, temp);
        excl = temp;
    # }
    return max(incl, excl);


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

