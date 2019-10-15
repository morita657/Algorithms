class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memory = collections.defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in memory.keys():
                memory[nums[i]] += 1
            else:
                memory[nums[i]] = 1
        ans = 0
        for index, key in enumerate(memory):
            if memory[key] == 1:
                ans = key
        return ans


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashSet = []
        for i in range(len(nums)):
            if nums[i] in hashSet:
                index = hashSet.index(nums[i])
                hashSet.pop(index)
            else:
                hashSet.append(nums[i])
        return hashSet[-1]
