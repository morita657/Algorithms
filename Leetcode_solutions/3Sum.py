class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            first = nums[i]
            for j in range(i + 1, len(nums)):
                second = nums[j]
                for k in range(j + 1, len(nums)):
                    third = nums[k]
                    total = first + second + third
                    comb = [first, second, third]
                    comb.sort()
                    if total == 0 and comb not in output:
                        output.append(comb)
        return output


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
