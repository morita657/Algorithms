class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        for i in range(len(nums)):
            if ans[0] < 0 and nums[i] == target:
                ans[0] = i
            if ans[0] >= 0 and nums[i] == target:
                ans[1] = i
        if ans[0] >= 0 and ans[1] < 0:
            ans[1] = ans[0]
        return ans
