class Solution:
    def reverseWords(self, s: str) -> str:
        txt = s.split()
        ans = ""
        for i in range(len(txt)):
            ans += txt[i][::-1] + " "
        return ans[:-1]
