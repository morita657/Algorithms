class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small = float('inf')
        big = float('inf')
        for n in nums:
            if n <= small:
                small = n
            elif n <= big:
                big = n
            else:
                return True
        return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        res = []
        for n in nums:
            index = bisect.bisect_left(res, n)
            if index == len(res):
                res.append(n)
            else:
                res[index] = n
            if len(res) == 3:
                return True
        return False
