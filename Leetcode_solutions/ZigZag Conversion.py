class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        adjuster = 2
        rows = [[] for _ in range(numRows)]
        cr = 0
        flag = True
        for i in range(len(s)):
            rows[cr].append(s[i])
            if cr == 0:
                flag = True
            elif cr == len(rows) - 1:
                flag = False
            if flag:
                cr += 1
            else:
                cr -= 1
        ans = ""
        for j in range(len(rows)):
            ans += "".join(rows[j])
        return ans
