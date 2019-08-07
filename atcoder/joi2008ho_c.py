#!/bin/python

import math
import os
import random
import re
import sys


def run(p, count, output, sum, n, m):
    if count == int(n) and sum <= int(m) or sum not in output:
        output.append(sum)
        count = 1
        sum = 0
        # return
    # else:
    for i in range(len(p)):
        print 'count: ', count
        sum += int(p[i])
        # count += 1
        # print count, num
        run(p, count + 1, output, sum, n, m)
    # print 'output: ', output
    return max(output)


def main():
    f = open("input.txt", "r")
    contents = f.read().split()
    n, m, p = contents[0], contents[1], contents[2:]
    count = 1
    output = []
    sum = 0
    return run(p, count, output, sum, n, m)


main()
