class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.remove(S) == self.remove(T)

    def remove(self, word):
        ans = []
        for ch in word:
            if ch != "#":
                ans.append(ch)
            elif ans:
                ans.pop()
        return "".join(ans)
