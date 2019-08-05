#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    anagrams = 0
    substrings = {i: [] for i in range(1, len(s) + 1)}
    print substrings
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = " ".join(sorted(s[i:j]))
            for k in range(0, len(substrings[j - i])):
                if substrings[j - i][k] == substr:
                    anagrams += 1
            substrings[j - i].append(substr)
    return anagrams


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
