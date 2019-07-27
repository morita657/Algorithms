class Solution(object):
    def findTargetSumWays(self, nums, S):
        from collections import defaultdict
        memo = {0: 1}
        for x in nums:
            m = defaultdict(int)
            # print 'm: ', m
            for s, n in memo.iteritems():
                print s, n
                m[s + x] += n
                m[s - x] += n
            memo = m
        return memo[S]


s = Solution()
s.findTargetSumWays([1, 1, 1, 1, 1], 3)
