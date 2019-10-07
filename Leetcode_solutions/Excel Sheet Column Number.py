class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = []
        for i in range(len(s)):
            if i != len(s) - 1:
                ans.append((ord(s[i]) - 64) * 26**(len(s) - 1 - i))
            else:
                ans.append(ord(s[i]) - 64)
        return sum(ans)
