first = raw_input().split()
n, k = int(first[0]), int(first[1])
ds = raw_input().split()
cand = [int(i) for i in range(0, 10)]
for i in range(len(ds)):
    if int(ds[i]) in cand:
        cand.pop(cand.index(int(ds[i])))
cand.sort()  # the rest of candidates
length = len(str(n))


def dfs(cand, output, now):
    # print now
    if int(now) <= 10000:
        output.append(now)
        return
    for i in range(n, 10000):
        dfs(cand, output, now + str(cand[i]))
    return output


o = dfs(cand, [], str(n))
print o
for i in range(len(o)):
    if int(o[i]) >= n:
        print int(o[i])
        exit(0)
# 1000 8
# 1 3 4 5 6 7 8 9
