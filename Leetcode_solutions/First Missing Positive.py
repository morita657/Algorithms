class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        current = 1
        index = 0
        while index < len(nums):
            if nums[index] > 0:
                if nums[index] != current:
                    break
                else:
                    current += 1
            index += 1
        return current
