class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.dfs(s, [], ans)
        return ans

    def dfs(self, s, path, ans):
        if not s:
            ans.append(path)
            return
        else:
            for i in range(1, len(s) + 1):
                cur = s[:i]
                if cur == cur[::-1]:
                    self.dfs(s[i:], path + [s[:i]], ans)
