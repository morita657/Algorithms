class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, k + 1):
            now = nums.pop()
            nums.insert(0, now)
        return nums
