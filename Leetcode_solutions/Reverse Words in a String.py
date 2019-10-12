class Solution:
    def reverseWords(self, s: str) -> str:
        txt = s.split()
        ans = ""
        for i in range(len(txt) - 1, -1, -1):
            ans += txt[i] + " "
        return ans[:-1]
