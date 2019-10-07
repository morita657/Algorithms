class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        d = []
        candidates = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                d.append((nums1[i] + nums2[j], [nums1[i], nums2[j]]))
        ans = []
        d.sort()
        index = 0
        for i in range(len(d)):
            if k > 0:
                ans.append(d[i][1])
            k -= 1
        return ans
