class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                zero = nums[i]
                nums[i:] = nums[i + 1:]
                nums.append(zero)
        return nums
