class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        candidates.sort()
        self.search(candidates, target, ans, [], 0)
        return ans

    def search(self, candidates, target, ans, current, start):
        if target == 0:
            ans.append(current)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            # current.append(candidates[i])
            self.search(candidates, target -
                        candidates[i], ans, current + [candidates[i]], i)


s = Solution()
s.combinationSum([2, 3, 6, 7], 7)
