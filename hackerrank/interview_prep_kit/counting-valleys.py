#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    altitude = 0
    for current in range(len(s)):
        if s[current] == 'D':
            altitude -= 1
        else:
            if altitude == -1 and s[current] == 'U':
                valleys += 1
            altitude += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

