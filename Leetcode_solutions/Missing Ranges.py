class Solution(object):
    def findMissingRanges(self, A, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        A.append(upper + 1)
        pre = lower - 1
        for i in A:
            if (i == pre + 2):
                result.append(str(i - 1))
            elif (i > pre + 2):
                result.append(str(pre + 1) + "->" + str(i - 1))
            pre = i
        return result
