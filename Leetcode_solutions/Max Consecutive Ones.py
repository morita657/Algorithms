class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        soFar = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            if nums[i] != 1 or i == len(nums) - 1:
                soFar = max(soFar, current)
                current = 0
        return soFar
