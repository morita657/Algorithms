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
