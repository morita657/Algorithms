#!/bin/python

import math
import os
import random
import re
import sys

# brute force
# Complete the activityNotifications function below.


def activityNotifications(expenditure, d):
    # init
    trailingDays = []
    for i in range(d):
        trailingDays.append(expenditure[i])
    expenditure[d]
    index = d
    notification = 0
    m = 0
    while index < len(expenditure):
        m = median(trailingDays)
        todaysExpenditure = expenditure[index]
        if todaysExpenditure >= m * 2:
            notification += 1
        if index + 1 < len(expenditure):
            trailingDays.pop(0)
            index += 1
            trailingDays.append(expenditure[index])
        else:
            break
    return notification


def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1]) / 2.0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()


import sys
#sys.stdin = open("in", "r")
n, d = map(int, raw_input().split())
arr = map(int, raw_input().split())

dic = {}


def find(idx):
    s = 0
    for i in xrange(0, 200):
        freq = 0
        if i in dic:
            freq = dic[i]
        s = s + freq
        if s >= idx:
            return i


ans = 0
for i in xrange(0, n):
    val = arr[i]

    if i >= d:
        med = find(d / 2 + d % 2)

        if d % 2 == 0:
            ret = find(d / 2 + 1)
            if val >= med + ret:
                ans = ans + 1
        else:
            if val >= med * 2:
                ans = ans + 1

    if val not in dic:
        dic[val] = 0
    dic[val] = dic[val] + 1

    # print i,dic
    if i >= d:
        prev = arr[i - d]
        dic[prev] = dic[prev] - 1

print ans
