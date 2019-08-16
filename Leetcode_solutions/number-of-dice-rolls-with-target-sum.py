from collections import defaultdict


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        something = defaultdict(int)
        output = []
        rest = []
        d = arr1
        for i in range(len(arr1)):
            if arr1[i] in arr2:
                something[d[i]] += 1
            else:
                rest.append(arr1[i])
        rest.sort()
        for j in range(len(arr2)):
            for k in range(something[arr2[j]]):
                output.append(str(arr2[j]))
        output = output + rest
        return output
