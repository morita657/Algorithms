#!/bin/python

import math
import os
import random
import re
import sys

# Complete the substrCount function below.


def substrCount(n, s):
    count = 0
    i = 0
    while i < len(s):
        for j in range(i, len(s)):
            if check(s[i:j + 1]):
                count += 1
        i += 1
    return count


def check(substr):
    mid = len(substr) // 2
    if len(substr) % 2 == 0 and len(set(substr)) == 1:
        return substr[:mid] == substr[mid:]
    else:
        return substr[:mid] == substr[mid + 1:]


from collections import defaultdict


def substrCount(n, s):
    i = 0
    j = 0
    same_char_count = defaultdict()
    while(i < n):
        j += 1
        c = 1
        while j < n and s[i] == s[j]:
            j += 1
            c += 1
        ans += c * (c + 1)
        same_cahr_count[i] = c
        i = j
    for j in range(1, n):
        if s[j] == s[j - 1]:
            same_char_count[j] = same_char_count[j - 1]
        if s[j - 1] == s[j + 1] and s[j] != s[j - 1]:
            ans += min(same_char_count[j - 1], same_char_count[j + 1])
    return ans


def substrCount(n, s):
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0

# 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

# 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans
