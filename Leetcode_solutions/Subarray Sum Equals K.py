class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            sum = 0
            for end in range(i, len(nums)):
                sum += nums[end]
                if sum == k:
                    ans += 1
        return ans
