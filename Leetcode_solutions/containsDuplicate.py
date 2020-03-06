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


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashTable = collections.defaultdict(list)
        length = len(nums)
        for i in range(len(nums)):
            index = nums[i] % length
            if nums[index] in hashTable.keys():
                return True
            else:
                hashTable[index].append(nums[i])
        return False
        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_array = nums.sort()
        for index in range(1,len(sorted(nums))):
            if nums[index-1] == nums[index]:
                return True
        return False