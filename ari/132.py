N = 5
M = 3
x = [1, 2, 8, 4, 9]


def C(d):
    last = 0
    for i in range(1, M):
        crt = last + 1
        while crt < N and (x[crt] - x[last]) < d:
            crt += 1
        if crt == N:
            return False
        last = crt
    return True


def solve():
    x.sort()
    lb = 0
    ub = 100000

    while ub - lb > 1:
        mid = (lb + ub) / 2
        if C(mid):
            lb = mid
        else:
            ub = mid
    return lb


def main():
    return solve()


print(main())
