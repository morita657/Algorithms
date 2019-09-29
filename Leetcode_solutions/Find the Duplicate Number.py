class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memo = collections.defaultdict(int)
        for i in range(len(nums)):
            memo[nums[i]] += 1
        for index, key in enumerate(memo):
            if memo[key] >= 2:
                return key
        return -1


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = []
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.append(nums[i])
        return -1
