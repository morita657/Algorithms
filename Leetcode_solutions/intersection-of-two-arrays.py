class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res, set1, visited = [], set(nums1), set()
        for e in nums2:
            if e in set1 and e not in visited:
                res.append(e)
                visited.add(e)
            elif e not in set1:
                visited.add(e)
        return res


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet1 = set(nums1)
        numSet2 = set(nums2)
        seen = []
        for i in numSet2:
            if i in numSet1:
                seen.append(i)
        return seen
