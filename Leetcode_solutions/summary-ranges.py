class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        output = []
        for j in range(len(nums)):

            #             if current j+1 is the continuous number, no problem
            #              if the current not, store them
            #               and also, move the start location to j+1
            if j + 1 < len(nums):
                if nums[j + 1] == j + 1:
                    continue
                else:
                    output.append("{}->{}".format(nums[i], nums[j]))
                i = j + 1
            else:
                output.append("{}".format(nums[i]))
        return output
