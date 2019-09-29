class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            if leftsum == (S - leftsum - nums[i]):
                return i
            leftsum += nums[i]
        return -1
