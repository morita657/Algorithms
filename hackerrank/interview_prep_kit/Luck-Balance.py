
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.


def luckBalance(k, contests):
    res = 0
    imp_contest = []

    for i in range(len(contests)):
        a, b = contests[i][0], contests[i][1]
        if b == 0:
            res += a
        else:
            imp_contest.append(a)
    imp_contest.sort(reverse=True)
    res += sum(imp_contest[:min(k, len(imp_contest))])
    res -= sum(imp_contest[k:])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in xrange(n):
        contests.append(map(int, raw_input().rstrip().split()))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
