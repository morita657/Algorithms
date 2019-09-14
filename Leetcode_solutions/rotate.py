class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = nums[:]

        while k > 0:
            poped_val = nums.pop()
            nums.insert(0, poped_val)
            k -= 1
        return nums
