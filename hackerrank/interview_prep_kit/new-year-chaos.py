# #!/bin/python

# import math
# import os
# import random
# import re
# import sys

# # check if each element moved more than 2 indexes


# def check1(q, s):
#     i = 0
#     res = False
#     while i < len(q):
#         if q[i] - s[i] >= 3:
#             res = True
#         i += 1
#     return res

# # Complete the minimumBribes function below.


# def minimumBribes(q):
#     # generate the source q
#     source = []
#     res = ""
#     for i in range(1, len(q) + 1):
#         source.append(i)
#     if check1(q, source):
#         res = "Too chaotic"
#     else:
#         total = 0
#         index = 0
#         while index < len(q):
#             total += abs(q[index] - source[index])
#             # print("q[index] - source[index]: ", q[index], source[index])
#             if index < len(q) - 1:
#                 index += 1
#             else:
#                 break
#         res = total / 2
#     print(res)


# if __name__ == '__main__':
#     t = int(raw_input())

#     for t_itr in xrange(t):
#         n = int(raw_input())

#         q = map(int, raw_input().rstrip().split())

#         minimumBribes(q)

# # #############################################

# # t = int(raw_input())

# # for _ in range(t):
# #     n = int(raw_input())
# #     arr = map(int, raw_input().split())
# #     org = range(n + 1)
# #     pos = range(n + 1)
# #     cnt = [0] * (n + 1)
# #     ans = 0
# #     invalid = 0

# #     for i in xrange(n - 1, -1, -1):

# #         if invalid:
# #             break

# #         # Get position where arr[i] should have been if no one bribed after this point

# #         oldp = pos[arr[i]]

# #         # Get the position where arr[i] currently is.

# #         newp = i + 1

# #         # oldp != newp indicates that even after this point, bribes took place
# #         # counting the number of furthter bribes that took place to bring arr[i] to i

# #         while oldp != newp:

# #             ans = ans + 1

# #             # arr[i] is at the right of org[oldp + 1] in the given array
# #             # that means org[oldp + 1] bribed arr[i] at some point
# #             # so increasing its count by 1

# #             cnt[org[oldp + 1]] += 1

# #             if cnt[org[oldp + 1]] > 2:
# #                 invalid = 1
# #                 break

# #             # updating the original array to match the array after this bribe took place

# #             org[oldp], org[oldp + 1] = org[oldp + 1], org[oldp]

# #             # update the positions also due to the change
# #             # caused by bribe that took place so far

# #             pos[org[oldp]] = oldp
# #             pos[org[oldp + 1]] = oldp + 1

# #             oldp = oldp + 1

# #     if invalid:
# #         ans = "Too chaotic"

# #     print ans


# 1
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4

def minimumBribes(Q):
    #
    # initialize the number of moves
    moves = 0
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)
    Q = [P - 1 for P in Q]
    #
    # Loop through each person (P) in the queue (Q)
    for i, P in enumerate(Q):
        # i is the current position of P, while P is the
        # original position of P.
        #
        # First check if any P is more than two ahead of
        # its original position
        if P - i > 2:
            print("Too chaotic")
            return
        #
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(P - 1, 0), i):
            print('i: ', i, 'Q[j]: ', Q[j], 'P: ', P, Q[j] > P)
            if Q[j] > P:
                moves += 1
    print(moves)


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
