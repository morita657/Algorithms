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
# For certain test cases with not very large nn, the runtime of this method can be slower than Approach #2. The reason is hash table has some overhead in maintaining its property. One should keep in mind that real world performance can be different from what the Big-O notation says. The Big-O notation only tells us that for sufficiently large input, one will be faster than the other. Therefore, when nn is not sufficiently large, an O(n)O(n) algorithm can be slower than an O(n \log n)O(nlogn) algorithm.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_array = nums.sort()
        for index in range(1,len(sorted(nums))):
            if nums[index-1] == nums[index]:
                return True
        return False