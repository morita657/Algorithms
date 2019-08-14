def main(friends):
    maxSoFar = 0
    for i in range(len(friends)):
        cnt = 0
        for j in range(len(friends[i])):
            if i == j:
                continue
            if friends[i][j] == 'Y':
                cnt += 1
            else:
                for k in range(len(friends[j])):
                    if friends[j][k] == 'Y' and friends[k][i] == 'Y':
                        cnt += 1
                        break
        maxSoFar = max(maxSoFar, cnt)
    return maxSoFar


print(main(["NNN", "NNN", "NNN"]))
print(main(["NYY", "YNY", "YYN"]))
print(main(["NYNNN", "YNYNN", "NYNYN", "NNYNY", "NNNYN"]))
print(main(["NNNNYNNNNN", "NNNNYNYYNN", "NNNYYYNNNN", "NNYNNNNNNN", "YYYNNNNNNY",
            "NNYNNNNNYN", "NYNNNNNYNN", "NYNNNNYNNN", "NNNNNYNNNN", "NNNNYNNNNN"]))
