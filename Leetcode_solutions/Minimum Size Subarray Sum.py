class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 1 and sum(nums) >= s:
            return 1
        elif len(nums) == 1 and sum(nums) == 0:
            return nums[0]
        elif len(nums) == 1 and sum(nums) < s:
            return 0
        if len(nums) == 0 and s >= 0:
            return 0

        ans = []
        current = []
        for i in range(len(nums)):
            current.append(nums[i])
            if sum(current) >= s:
                ans.append((len(current), current))
            for j in range(i + 1, len(nums)):
                current.append(nums[j])
                if sum(current) >= s:
                    ans.append((len(current), current))
            current = []
        ans.sort()
        if len(ans) > 0:
            return ans[0][0]
        else:
            return 0


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 1 and sum(nums) >= s:
            return 1
        elif len(nums) == 1 and sum(nums) == 0:
            return nums[0]
        elif len(nums) == 1 and sum(nums) < s:
            return 0
        if len(nums) == 0 and s >= 0:
            return 0

        ans = []
        current = []
        for i in range(len(nums)):
            current.append(nums[i])
            if sum(current) >= s:
                ans.append((len(current), current))
                while sum(current) >= s:
                    ans.append((len(current), current))
                    current.pop(0)
        ans.sort()
        if len(ans) > 0:
            return ans[0][0]
        else:
            return 0


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = left = right = 0
        res = len(nums) + 1
        while right < len(nums):
            total += nums[right]
            while total >= s:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return res if res <= len(nums) else 0
