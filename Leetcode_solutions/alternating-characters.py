#!/bin/python

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.


def alternatingCharacters(s):
    counter = 0
    current = s[0]
    for c in range(1, len(s)):
        if s[c] == current:
            counter += 1
        else:
            current = s[c]
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
