import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = math.floor(len(nums) / 2)
        flag = True
        index = -1
        left = nums[:mid]
        right = nums[mid:]
        for i in range(len(left)):
            if left[i] == target:
                index = nums.index(left[i])
        for j in range(len(right)):
            if right[j] == target:
                index = nums.index(right[j])
        return index
