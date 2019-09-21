class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxInd = -float('Inf')
        if len(nums) == 0:
            return maxInd
        if len(nums) == 1:
            return 0
        soFar = nums[0]
        maxInd = 0
        for i in range(1, len(nums)):
            if nums[i] > soFar:
                soFar = nums[i]
                maxInd = i
        return maxInd
