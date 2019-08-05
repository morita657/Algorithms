#!/bin/python

import math
import os
import random
import re
import sys

N = 1
M = 1
field = []

for n in range(0, N):
    field.append([])
    for m in range(0, M + 1):
        field[n].append([])


def dfs(x, y):
    field[x][y] = '.'

    for dx in range(-1, 1):
        for dy in range(-1, 1):
            nx = x + dx
            ny = y + dy

            if 0 <= nx and nx < N and 0 <= ny and ny < M and field[nx][ny] == 'W':
                dfs(nx, ny)
    return 0


def main():
    res = 0
    for i in range(0, N):
        for j in range(0, M):
            if field[i][j] == 'W':
                dfs(i, j)
                res += 1
    print res
    return


main()
