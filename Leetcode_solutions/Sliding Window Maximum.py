class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        output = []
        left = 0
        right = k
        while right <= len(nums):
            current = max(nums[left:right])
            output.append(current)
            left += 1
            right += 1
        return output
