class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        current = nums[0]
        for num in range(1, len(nums)):
            current = current ^ nums[num]
        return current