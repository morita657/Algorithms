class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        flag = False
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if left + 1 == right and nums[mid] != target:
                break
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        flag = False
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
