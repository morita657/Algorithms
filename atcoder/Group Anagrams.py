class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for i in strs:
            d[tuple(sorted(i))].append(i)
        return d.values()
