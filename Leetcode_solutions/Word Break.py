from collections import deque


class Solution:
    def wordBreak(self, s, wordDict):
        queue = deque()
        visited = set()
        queue.appendleft(0)
        visited.add(0)
        while len(queue) > 0:
            curr_index = queue.pop()
            for i in range(curr_index, len(s) + 1):
                if i in visited:
                    continue
                if s[curr_index:i] in wordDict:
                    if i == len(s):
                        return True
                    queue.appendleft(i)
                    visited.add(i)
        return False


s = Solution()
s.wordBreak("leetcode", ["leet", "code"])
