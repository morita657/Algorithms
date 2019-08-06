#!/bin/python

import math
import os
import random
import re
import sys

N = 20
M = 10
field = []
f = open("input.txt", "r").read()

float("inf")
maze = []


def mazeInitializer():
    for line in f:
        maze.append(list(line.rstrip()))
    return maze


mazeInitializer()
# print maze
# for line in file:
#         maze.append(list(line.rstrip()))
# return maze
for n in range(N):
    maze.append([])
    for m in range(M):
        maze[n].append([])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def findStart(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 's':
                sx = i
                sy = j
                # print sx, i
                return tuple([i, j]), sx, sy


def findGoal(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'e':
                gx = i
                gy = j
                return gx, gy


start, sx, sy = findStart(maze)
gx, gy = findGoal(maze)


def bfs():
    que = []
    for i in range(N):
        for j in range(M):
            d[i][j] = float('inf')
    que.append(start)
    d[sx][sy] = 0

    while len(que):
        p = que[0]
        que.pop(0)
        print p
        if p[0][0] == gx and p[0][1] == gy:
            break
        for i in range(0, 4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if 0 <= nx and nx < N and 0 <= ny and ny < M and maze[nx][ny] != '#'and d[nx][ny] == float('inf'):
                que.append(p[nx][ny])
                d[nx][ny] = d[p[0]][d[1]] + 1
    return d[gx][gy]


def main():
    res = bfs()
    print res


main()
