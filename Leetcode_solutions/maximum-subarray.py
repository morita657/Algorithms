class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = nums[0]
        maxSeenSoFar = nums[0]
        for i in range(1, len(nums)):
            currentMax = max(nums[i], currentMax + nums[i])
            maxSeenSoFar = max(maxSeenSoFar, currentMax)
        return maxSeenSoFar
