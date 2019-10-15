class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        pairs = []
        ans = 0
        nums.sort()
        for i in range(1, len(nums), 2):
            pairs.append([nums[i - 1], nums[i]])
        for j in range(len(pairs)):

            ans += min(pairs[j])
        return ans
