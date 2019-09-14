class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memory = []
        for i in range(len(nums)):
            if nums[i] in memory:
                return True
            else:
                memory.append(nums[i])
        return False
