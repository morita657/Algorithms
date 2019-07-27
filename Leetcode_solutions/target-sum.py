class Solution(object):
    def __init__(self):
        self.cnt = 0

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        i = 0
        current = 0
        self.compute(nums, S, i, current)
        return self.cnt

    def compute(self, nums, S, index, v):
        if index == len(nums):
            if v == S:
                self.cnt = self.cnt + 1
        else:
            self.compute(nums, S, index + 1, v + nums[index])
            self.compute(nums, S, index + 1, v - nums[index])
