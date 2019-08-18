# sort-an-array
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        pivot = int(len(nums)) / 2
        left = sortArray(nums[0:pivot])
        right = sortArray(nums[pivot:])

        return self.merge(left, right)

    def merge(self, left, right):
        left_cursor = right_cursor = 0
        ret = []
        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] < right[right_cursor]:
                ret.append(left[left_cursor])
                left_cursor += 1
            else:
                ret.append(right[right_cursor])
                right_cursor += 1

        ret.extend(left[left_cursor:])
        ret.extend(right[right_cursor:])
        return ret
