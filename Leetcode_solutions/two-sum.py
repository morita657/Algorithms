class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    break
        return ans


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        q = nums[:]
        while True:
            now = q[0]
            index = nums.index(now)
            q.pop(0)
            for i in range(index + 1, len(nums)):
                if now + nums[i] == target:
                    return [index, i]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = collections.defaultdict(list)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict.keys():
                return [dict[complement][0], i]
            dict[nums[i]].append(i)

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if map[complement] and map[complement] != i:
                return [i, map[complement]]

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)        
        for i in range(len(nums)):
            complement = target - nums[i]
            if str(complement) in map and map.get(str(complement)) != i:
                return [i, map[str(complement)]]
            map[str(nums[i])]=i