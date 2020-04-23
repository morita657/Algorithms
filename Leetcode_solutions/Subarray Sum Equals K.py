class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            sum = 0
            for end in range(i, len(nums)):
                sum += nums[end]
                if sum == k:
                    ans += 1
        return ans


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            total = 0
            for end in range(start, len(nums)):
                total += nums[end]
                if total == k:
                    count += 1
        return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        preSum, ret, size = [0], 0, len(nums)
        count = collections.Counter(preSum)
        if size == 1:
            return 1 if nums[0] == k else 0
        for val in nums:
            s = preSum[-1] + val
            preSum.append(s)
            ret += count.get(s - k, 0)
            count[s] = count.get(s, 0) + 1

        return ret
        
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        total=0
        hashmap = defaultdict(int)
        hashmap[0]=1
        for i in range(len(nums)):
            total += nums[i]
            if total-k in hashmap.keys():
                count += hashmap.get(total-k)
            hashmap[total]=hashmap[total]+1
        return count