class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        maxSoFar = 1
        currentMax = 1
        tracker = nums[0]
        for i in range(1, len(nums)):
            tracker += 1
            if tracker == nums[i]:
                currentMax += 1
            else:
                tracker = nums[i]
                currentMax = 1
            maxSoFar = max(currentMax, maxSoFar)
        return maxSoFar
