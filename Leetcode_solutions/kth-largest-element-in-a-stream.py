# brute force
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.nums.append(float("inf"))

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort()
        target = 0
        self.nums.reverse()
        index = 1
        while index < len(self.nums):
            if index == self.k:
                target = self.nums[index]
            index += 1
        return target


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
