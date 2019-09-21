class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums) or len(nums) == 0:
            return -1
        nums.sort()
        return nums[-k]


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]
