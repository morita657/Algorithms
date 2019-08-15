W = raw_input()
limit = raw_input().split()
n, K = int(limit[0]), int(limit[1])
shots = []
for _ in range(n):
    shot = raw_input().split()
    shots.append([int(shot[0]), int(shot[1])])
s = 0  # curretn total priority
w = 0  # current total width
cnt = 0
ret = 0
dp = []
for i in range(n + 1):
    dp.append([])
    for j in range(len(shots[0]) * len(shots[1])):
        dp[i].append(0)


def main(i, w, cnt):
    if i == n:
        res = 0
    elif w < shots[i][0]:
        res = main(i + 1, w, cnt)
    else:
        res = max(main(i + 1, w - shots[i][0], cnt + 1) + shots[i][1],
                  main(i + 1, w, cnt))
    return res


print main(0, int(W), 0)
