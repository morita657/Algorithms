import bisect
n = 10
S = 15
a = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
s = [0 for i in range(n + 1)]


def main():
    cnt = 0
    res = n + 1
    s = 0
    t = 0
    sum = 0
    for i in range(n):
        while t < n and sum < S:
            # t += 1
            sum += a[t + 1]
        if sum < S:
            break
        # res = min(res, t - s)

        sum -= a[s + 1]
    if res >= n:
        cnt += 1
        res = 0
    print(res)
    print('sum: ', sum, cnt)


main()
