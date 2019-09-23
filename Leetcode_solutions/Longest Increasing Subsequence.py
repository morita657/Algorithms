
class Solution:
    def lengthOfLIS(self, nums):
        return self.main(nums, -float('inf'), 0)

    def main(nums, prev, curpos):
        if curpos == len(nums):
            return 0
        taken = 0
        if nums[curpos] > prev:
            taken = 1 + self.main(nums, nums[curpos], curpos + 1)
        nottaken = self.main(nums, prev, curpos + 1)
        return max(taken, nottaken)


s = Solution()
s.lengthOfLIS([10, 9, 2, 5, 3, 4])


class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1 for x in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
