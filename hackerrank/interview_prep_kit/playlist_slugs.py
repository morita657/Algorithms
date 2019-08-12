#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.

# brute force


def arrayManipulation(n, queries):
    source = []
    for i in range(n):
        source.append(0)

    for i in range(len(queries)):
        for j in range(queries[i][0] - 1, queries[i][1]):
            source[j] += queries[i][2]
    return max(source)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()


# Optimal solution
#!/bin/python

import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):
    v = []
    for a0 in range(len(queries)):
        v.append((queries[a0][0], queries[a0][2]))
        v.append((queries[a0][1] + 1, -1 * queries[a0][2]))
    mx = 0
    sum = 0
    v.sort()
    for i in range(2 * len(queries)):
        sum += v[i][1]
        mx = max(mx, sum)
    return mx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
