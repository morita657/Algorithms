# the types of coins
V = [1, 5, 10, 50, 100, 500]
# the number of coins
C = [3, 2, 1, 3, 0, 2]


def main():
    A = 620
    ans = 0
    output = []
    for m in reversed(range(len(V))):
        # print V[m]
        temp = min(A/V[m], C[m])
        print "temp: ", temp, A/V[m], C[m]
        A -= temp*V[m]
        ans += temp
    # print output
    print ans
    return 0


main()
