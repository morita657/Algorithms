class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = []
        for i in range(len(nums)):
            current = nums[i]
            for j in range(i + 1, len(nums)):
                current *= nums[j]
                output.append(current)
        return max(output)
