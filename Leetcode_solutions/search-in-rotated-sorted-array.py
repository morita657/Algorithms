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


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
