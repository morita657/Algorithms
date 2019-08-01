#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cnt = 0
    index = 0
    while index < len(c)-1:
        # try to take 2 steps if the target is not a thunderhead
        if index+2 <= len(c)-1:
            if c[index+2] == 0:
                index += 1
        # else take 1 step if the target is not a thunderhead
        index += 1
        cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

