def main(s):
    ans = 0
    i = len(s)
    while True:
        flag = True
        for j in range(len(s)):
            if (i - j - 1) < len(s) and s[i - j - 1] != s[j]:
                flag = False
                break
        if flag:
            return i
        i += 1
    return


print(main('abab'))
print(main('abacaba'))
print(main('qwerty'))
