#!/bin/python

import math
import os
import random
import re
import sys


def main():
    f = open("input.txt", "r")
    contents = f.read().split()
    n, m = contents[0], contents[1:]
    output = []
    i = 0
    j = 2
    while i < len((m)):
        while j < len((m)):
            res = math.sqrt(
                pow(int(m[j + 1]) - int(m[i + 1]), 2) + pow(int(m[j]) - int(m[i]), 2))
            output.append(res)
            j += 2
        i += 2
    print output
    print "%.6f" % max(output)
    return


main()
