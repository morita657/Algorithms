class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
        current = 0
        ans = None
        for index, key in enumerate(d):
            if d[key] > current:
                current = d[key]
                ans = key
        return ans
