#!/bin/python

import math
import os
import random
import re
import sys

# bipartite graph
MAX_V = 1000
G = []
G[MAX_V]  # GRAPH
V  # VERGE
color = []
color[MAX_V]  # COLOR AT VERGE I


def dfs(v, c):
    color[v] = c
    for i in range(0, len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True


def solve():
    for i in range(0, V):
        if color[i] == 0:
            if not dfs(i, 1):
                print("NO")
                return
    print("YES")
