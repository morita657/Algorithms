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


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def search(nums, l, r):
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return search(nums, l, mid)
            return search(nums, mid + 1, r)
        return search(nums, 0, len(nums) - 1)
