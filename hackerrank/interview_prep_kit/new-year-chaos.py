#!/bin/python

import math
import os
import random
import re
import sys

# check if each element moved more than 2 indexes


def check1(q, s):
    i = 0
    while i < len(q):
        res = False
        if abs(q[i] - s[i]) >= 3:
            return True
        i += 1
    return res

# Complete the minimumBribes function below.


def minimumBribes(q):
    # generate the source q
    source = []
    res = ""
    for i in range(1, len(q) + 1):
        source.append(i)
    if check1(q, source):
        res = "Too chaotic"
    else:
        total = 0
        index = 0
        while index <= len(q):
            total += abs(q[i] - source[i])
            if index < len(q):
                index += 1
            else:
                break
        res = total / 2

    return res


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)

# #############################################

# t = int(raw_input())

# for _ in range(t):
#     n = int(raw_input())
#     arr = map(int, raw_input().split())
#     org = range(n + 1)
#     pos = range(n + 1)
#     cnt = [0] * (n + 1)
#     ans = 0
#     invalid = 0

#     for i in xrange(n - 1, -1, -1):

#         if invalid:
#             break

#         # Get position where arr[i] should have been if no one bribed after this point

#         oldp = pos[arr[i]]

#         # Get the position where arr[i] currently is.

#         newp = i + 1

#         # oldp != newp indicates that even after this point, bribes took place
#         # counting the number of furthter bribes that took place to bring arr[i] to i

#         while oldp != newp:

#             ans = ans + 1

#             # arr[i] is at the right of org[oldp + 1] in the given array
#             # that means org[oldp + 1] bribed arr[i] at some point
#             # so increasing its count by 1

#             cnt[org[oldp + 1]] += 1

#             if cnt[org[oldp + 1]] > 2:
#                 invalid = 1
#                 break

#             # updating the original array to match the array after this bribe took place

#             org[oldp], org[oldp + 1] = org[oldp + 1], org[oldp]

#             # update the positions also due to the change
#             # caused by bribe that took place so far

#             pos[org[oldp]] = oldp
#             pos[org[oldp + 1]] = oldp + 1

#             oldp = oldp + 1

#     if invalid:
#         ans = "Too chaotic"

#     print ans


# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
