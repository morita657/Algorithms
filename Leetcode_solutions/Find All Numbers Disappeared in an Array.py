class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        j = 1
        for i in range(len(nums)):
            if nums[i] != j and j not in nums:
                ans.append(j)
            j += 1
        return ans


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set(nums)
        return [i for i in range(1, len(nums) + 1) if not i in seen]
