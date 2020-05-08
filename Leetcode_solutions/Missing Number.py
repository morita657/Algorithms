class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        index = 0
        for i in range(len(nums)):
            if index != nums[i]:
                return index
            index += 1
        return index
        

class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = ((len(nums)) * (len(nums)+1)) // 2
        current_total = sum(nums)
        return (total - current_total)