class Solution:
    current = 0

    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            first = nums[i] + nums[i - 2]
            second = max(nums[i - 2], nums[i - 1])
            current = max(first, second)
        return current
