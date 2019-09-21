import heapq
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = defaultdict(int)
        pq = []
        # count frequency by index
        for i in nums:
            freq[i] += 1
        # pair (freq and index) in heap
        for key in freq:
            heapq.heappush(pq, (freq[key], key))
        result = []
        # grab k largest elements
        temp = heapq.nlargest(k, pq)
        # push the index numbers
        for j in range(len(temp)):
            result.append(temp[j][1])
        return result


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return None
        d = collections.defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
        ans = []
        for index, key in enumerate(d):
            ans.append((d[key], key))
        ans.sort()
        ans = ans[::-1]
        res = []
        for i in range(k):
            res.append(ans[i][1])
        return res


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
